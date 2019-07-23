"""Lunch Poll model forms"""

from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from .models import Menu


class MenuForm(forms.ModelForm):
    """Form to create new menus"""
    class Meta:
        model = Menu
        fields = ['menu_intro', 'menu_date']

    menu_intro = forms.CharField()
    menu_date = forms.DateField(widget=forms.SelectDateWidget)

    def clean_menu_date(self):
        """Check if a date is not in the past"""

        menu_date = self.cleaned_data['menu_date']
        if menu_date < date.today():
            raise ValidationError(('Invalid date - Menu in past'))

        return menu_date
