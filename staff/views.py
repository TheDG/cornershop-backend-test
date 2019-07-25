"""Staff views."""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.contrib.auth import login
from django.db.models import F
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cryptography.fernet import Fernet
from lunch_poll.models import Menu, Option
from .forms import SelectionForm
from .models import Selection


def menu(request, menu_uuid):
    """Staff show menu"""
    selected_menu = get_object_or_404(Menu, uuid=menu_uuid)
    encrypted_user = request.GET.get('user', '')
    f = Fernet(selected_menu.key)
    try:
        username = f.decrypt(bytes(encrypted_user, 'utf-8')).decode('utf-8')
    except:
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
            form.custom_validation(request.user)
        except ValidationError as errors:
            for error in errors:
                messages.error(request, error)
        if form.is_valid():
            print("shiit")
            # TODO: Transaction
            selected_option = Option.objects.get(pk=request.POST['option'])
            selected_option.votes = F('votes') + 1
            selected_option.save()
            form.save()
            messages.success(request, 'Succesfully choose menu option')
        else:
            print(form.errors, len(form.errors))
    logout(request)
    return render(request, ('pages/index.html'))
