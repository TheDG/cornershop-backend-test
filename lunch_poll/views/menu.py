"""Lunch Poll menu views / router."""

from django.contrib.auth.decorators import login_required, permission_required
from lunch_poll.forms import MenuForm
from lunch_poll.models import Menu
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu(request):
    # create action
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: redirect to show
            return HttpResponseRedirect(reverse('lunch_poll:index'))
        return render(request, 'lunch_poll/menu/new.html', {'form': form})
    # Index action
    else:
        print("has")
        menus = Menu.objects.all()
        return render(request,'lunch_poll/menu/index.html', {'menus':menus})

@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu_new(request):
    form = MenuForm()
    return render(request, 'lunch_poll/menu/new.html', {'form': form})
