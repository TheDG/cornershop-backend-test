"""Lunch Poll model forms"""

from django import forms
from django.core.exceptions import ValidationError
from .models import Selection


class SelectionForm(forms.ModelForm):
    """Form to create new selection"""
    class Meta:
        model = Selection
        fields = ['option', 'menu', 'customization']

    def __init__(self, *args, **kwargs):
        self.option = args[0].get('option')
        self.menu = args[0].get('menu')
        self.customization = args[0].get('customization')
        super(SelectionForm, self).__init__(*args, **kwargs)

    def custom_validation(self, user):
        """Custom validation to check user has not selected option for this menu"""
        selection = Selection.objects.filter(selected_by=user, menu=self.menu)
        if selection.exists():
            raise ValidationError(
                ('User already chose selection for this menu'))
