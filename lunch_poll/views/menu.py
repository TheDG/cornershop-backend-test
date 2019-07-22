"""Lunch Poll menu views / router."""

from django.contrib.auth.decorators import login_required, permission_required
from lunch_poll.forms import MenuForm
from lunch_poll.models import Menu
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu(request):
    # create action
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: THink about redirect
            return HttpResponseRedirect(reverse('lunch_poll:index'))
        return render(request, 'lunch_poll/menu/new.html', {'form': form})
    # Index action
    else:
        menus = Menu.objects.all().order_by('menu_date')
        paginator = Paginator(menus, 10)
        page = request.GET.get('page')
        menus = paginator.get_page(page)
        return render(request, 'lunch_poll/menu/index.html', {'menus': menus})


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu_new(request):
    form = MenuForm()
    return render(request, 'lunch_poll/menu/new.html', {'form': form})


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.view_menu')
def menu_show(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'lunch_poll/menu/show.html', {'menu': menu})
