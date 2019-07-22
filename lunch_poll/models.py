import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
    menu_intro = models.CharField(max_length=200)
    menu_date = models.DateField()

    def __str__(self):
        return self.menu_date

    def is_active(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.menu_date <= now

    is_active.short_description = 'Can still make a choice?'
    is_active.boolean = True

class Options(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
