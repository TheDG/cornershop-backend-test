from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_intro', 'menu_date']

    menu_intro = forms.CharField()
    menu_date = forms.DateField(initial=date.today, widget=forms.SelectDateWidget)

    def clean_menu_date(self):
        menu_date = self.cleaned_data['menu_date']

        # Check if a date is not in the past.
        if menu_date < date.today():
            raise ValidationError(('Invalid date - Menu in past'))

        return menu_date
