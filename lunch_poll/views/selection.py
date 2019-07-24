"""Lunch Poll menu vote, selection creater / router."""

from django.db.models import F
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from lunch_poll.forms import SelectionForm
from lunch_poll.models import Option


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_selection')
def selection_new(request):
    """Post action for selecton, missing refactor"""
    if request.method == "POST":
        form = SelectionForm(request.POST)
        form.instance.selected_by = request.user
        try:
            form.custom_validation(request.user)
        except ValidationError as errors:
            for error in errors:
                messages.error(request, error)
            return HttpResponseRedirect(
                reverse('lunch_poll:menu_show',
                        kwargs={'menu_id': request.POST.get('menu')}))
        if form.is_valid():
            # TODO: Transaction
            selected_option = Option.objects.get(pk=request.POST['option'])
            selected_option.votes = F('votes') + 1
            selected_option.save()
            form.save()
            messages.success(request, 'Succesfully choose menu option')
    return render(request, ('pages/index.html'))