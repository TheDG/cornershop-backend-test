"""Lunch Poll views / router."""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from .forms import MenuForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class IndexView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """Admin main page"""
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    template_name = 'lunch_poll/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        """Meanwhile return nothing"""
        return []

    def test_func(self):
        """Only Admin users can access this view"""
        return self.request.user.is_superuser

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
    #else:

@login_required(login_url='/accounts/login/')
@permission_required('lunch_poll.add_menu')
def menu_new(request):
    form = MenuForm()
    return render(request, 'lunch_poll/menu/new.html', {'form': form})
