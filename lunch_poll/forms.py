"""Lunch Poll model forms"""

from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit, Row
from .custom_layout_object import Formset
from .models import Menu, Option, Selection


class MenuForm(forms.ModelForm):
    """Form to create new menus"""
    class Meta:
        model = Menu
        fields = ['menu_intro', 'menu_date']

    menu_date = forms.DateField(widget=forms.SelectDateWidget)
    menu_intro = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_show_errors = False
        self.helper.form_class = ''
        self.helper.label_class = 'col-3'
        self.helper.field_class = 'col-9'
        self.helper.layout = Layout(
            Row(Field('menu_date', css_class="mb-2")),
            Row(Field('menu_intro', css_class="col-12")),
            HTML("<hr>"),
            Row(
                Fieldset('Add choices', Formset('choice_text')),
                HTML("<hr>"),
                css_class="d-block text-center"
            ),
            ButtonHolder(Submit('submit', 'save'),
                         css_class="d-block btn-block")
        )

    def clean_menu_date(self):
        """Check if a date is not in the past"""
        menu_date = self.cleaned_data['menu_date']
        if menu_date < date.today():
            raise ValidationError(('Invalid date - Menu in past'))
        return menu_date


class OptionForm(forms.ModelForm):
    """Inline form for option"""
    class Meta:
        model = Option
        fields = ['choice_text']
    choice_text = forms.CharField(widget=forms.Textarea)


OPTION_FORM_SET = inlineformset_factory(
    Menu, Option, form=OptionForm,
    fields=['choice_text'], extra=3, can_delete=True
)

OPTION_FORM_SET_UPDATE = inlineformset_factory(
    Menu, Option, form=OptionForm,
    fields=['choice_text'], extra=0, can_delete=True
)

class SelectionForm(forms.ModelForm):
    """Form to create new selection"""
    class Meta:
        model = Selection
        fields = ['option', 'menu']

    def __init__(self, *args, **kwargs):
        self.option = args[0].get('option')
        self.menu = args[0].get('menu')
        super(SelectionForm, self).__init__(*args, **kwargs)


    def custom_validation(self, user):
        selection = Selection.objects.filter(selected_by=user, menu=self.menu)
        if selection.exists():
            raise ValidationError(('User already chose selection for this menu'))
