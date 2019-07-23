"""Lunch Poll models"""

from django.db import models
from django.utils import timezone


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


class Options(models.Model):
    """Options model."""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
