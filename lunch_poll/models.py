"""Lunch Poll models"""

import uuid
import os
import base64
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import slack
load_dotenv()


def generate_key():
    """Geneate a url safe base64 encoded key"""
    password = os.getenv("PASSWORD").encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password)).decode('utf-8')


def encrypted_user(user, menu):
    """AES encryption of username"""
    encoded = user.username.encode()
    fernet = Fernet(menu.key)
    return fernet.encrypt(encoded).decode('utf-8')


class Menu(models.Model):
    """Menu model."""
    menu_intro = models.CharField(max_length=200)
    menu_date = models.DateField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    key = models.CharField(max_length=200, default=generate_key)

    def __str__(self):
        return self.menu_intro

    def is_active(self):
        """Returns true if menu is not on the past / been served."""
        now = timezone.now().date()
        return now <= self.menu_date

    is_active.short_description = 'Can still make a choice?'
    is_active.boolean = True

    def votes(self):
        """Return the total amount of selections"""
        options = Option.objects.filter(menu=self)
        return options.aggregate(Sum('votes'))['votes__sum']

    def send_slack(self, request):
        """Send slack reminders to each user"""
        users = User.objects.filter(is_active=True, is_superuser=False)
        client = slack.WebClient(token=os.getenv("SLACK_API_TOKEN"))
        host = request.get_host()
        for user in users:
            url_user = encrypted_user(user, self)
            try:
                client.chat_postMessage(
                    channel=f"@{user.username}",
                    text=f"Click to order lunch: http://{host}/menu/{self.uuid}?user={url_user}",
                    as_user=True)
            except Exception:
                messages.error(
                    request, f"Couldn't send notification to {user.email}")


class Option(models.Model):
    """Options model."""
    menu = models.ForeignKey(
        Menu, related_name="has_options", on_delete=models.CASCADE)
    choice_text = models.TextField(verbose_name="Choice")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
