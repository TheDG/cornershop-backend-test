"""Lunch Poll models"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum


class Menu(models.Model):
    """Menu model."""
    menu_intro = models.CharField(max_length=200)
    menu_date = models.DateField(unique=True)

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


class Option(models.Model):
    """Options model."""
    menu = models.ForeignKey(
        Menu, related_name="has_options", on_delete=models.CASCADE)
    choice_text = models.TextField(verbose_name="Choice")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Selection(models.Model):
    """User selection model."""
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    selected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # SHould be normalized, but for simplicity using redundant data
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customization = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['menu', 'selected_by'], name='just on selection per day')
        ]

    def __str__(self):
        return str(self.id)
