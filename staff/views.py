"""Staff views."""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.exceptions import ValidationError
from cryptography.fernet import Fernet
from lunch_poll.models import Menu, Option
from .forms import SelectionForm
from .models import Selection


# TODO: REFactor this method
def menu(request, menu_uuid):
    """Staff show menu"""
    selected_menu = get_object_or_404(Menu, uuid=menu_uuid)
    encrypted_user = request.GET.get('user', '')
    fernet = Fernet(selected_menu.key)
    try:
        username = fernet.decrypt(
            bytes(encrypted_user, 'utf-8')).decode('utf-8')
    except Exception:
        return HttpResponseBadRequest("Corrupt Link + Data")
    user = get_object_or_404(User, username=username)
    login(request, user)
    selection = Selection.objects.filter(selected_by=user, menu=selected_menu)
    if not selection.exists():
        return render(request, 'staff/menu/show.html', {'menu': selected_menu})
    return render(request, 'staff/selection/show.html',
                  {'menu': selected_menu, 'selection': selection.first()})


@login_required(login_url='/accounts/login/')
def selection_new(request):
    """Post action for selecton, missing refactor"""
    if request.method == "POST":
        form = SelectionForm(request.POST)
        form.instance.selected_by = request.user
        try:
            # TODO: Couldnt do it all in clean form method
            form.unique_selection_validation(request.user)
            form.time_validation()
        except ValidationError as errors:
            for error in errors:
                messages.error(request, error)
        else:
            # TODO:TRansaction
            selected_option = Option.objects.get(pk=request.POST['option'])
            selected_option.votes = F('votes') + 1
            selected_option.save()
            form.save()
            messages.success(request, 'Succesfully choose menu option')
    logout(request)
    return render(request, ('pages/index.html'))
