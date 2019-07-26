"""Staff Selection model forms"""

from django import forms
from django.utils import timezone
from lunch_poll.models import Menu
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

    # Couldn't get clean to work
    def unique_selection_validation(self, user):
        """Custom validation to check user has not selected option for this menu"""
        selection = Selection.objects.filter(selected_by=user, menu=self.menu)
        if selection.exists():
            raise forms.ValidationError(
                'User already chose selection for this menu')

    # Couldn't get clean to work
    def time_validation(self):
        """Custom validation to check if request is before today at 11 am """
        menu_date = Menu.objects.get(pk=self.menu).menu_date
        now = timezone.now()
        cut_off_time = timezone.now().replace(hour=11, minute=0, second=0, microsecond=0)
        now_date = timezone.now().date()
        if menu_date < now_date:
            raise forms.ValidationError('This is a past menu')
        if now_date == menu_date and timezone.localtime(now) > cut_off_time:
            raise forms.ValidationError('You are to late')
