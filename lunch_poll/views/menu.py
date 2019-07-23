"""Lunch Poll menu views / router."""

from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from lunch_poll.forms import MenuForm
from lunch_poll.models import Menu, Option
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from lunch_poll.forms import OptionFormSet, OptionFormSetUpdate

class MenuCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Menu
    template_name = 'lunch_poll/menu/new.html'
    form_class = MenuForm

    success_url = None
    permission_required = 'lunch_poll.add_menu'

    def get_initial(self, **kwargs):
        if 'menu_date' in self.kwargs:
            return {'menu_date': self.kwargs['menu_date']}
        else:
            return {'menu_date': timezone.now().date()}


    def get_context_data(self, **kwargs):
        data = super(MenuCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['choice_text'] = OptionFormSet(self.request.POST)
        else:
            data['choice_text'] = OptionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choice_text = context['choice_text']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if choice_text.is_valid():
                choice_text.instance = self.object
                choice_text.save()
        return super(MenuCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('lunch_poll:index')


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu(request):
    """Menu index controller"""
    menus = Menu.objects.all().order_by('menu_date')
    paginator = Paginator(menus, 10)
    page = request.GET.get('page')
    menus = paginator.get_page(page)
    return render(request, 'lunch_poll/menu/index.html', {'menus': menus})


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.view_menu')
def menu_show(request, menu_id):
    """Get menu with id and show"""
    current_menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'lunch_poll/menu/show.html', {'menu': current_menu})


@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.delete_menu')
def menu_destroy(request, menu_id):
    """Delete menu"""
    current_menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        current_menu.delete()
    menus = Menu.objects.all().order_by('menu_date')
    paginator = Paginator(menus, 10)
    page = request.GET.get('page')
    menus = paginator.get_page(page)
    return render(request, 'lunch_poll/menu/index.html', {'menus': menus})

class MenuUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView ):
    model = Menu
    template_name = 'lunch_poll/menu/new.html'
    form_class = MenuForm

    permission_required = 'lunch_poll.add_menu'


    def get_context_data(self, **kwargs):
        data = super(MenuUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['choice_text'] = OptionFormSetUpdate(self.request.POST, instance=self.object)
        else:
            data['choice_text'] = OptionFormSetUpdate(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['choice_text']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(MenuUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('lunch_poll:index')
