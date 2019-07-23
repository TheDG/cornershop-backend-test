"""Lunch Poll index views / router."""
# pylint: disable=W0221

import datetime
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from lunch_poll.models import Menu


class IndexView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """Admin main page"""
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    template_name = 'lunch_poll/index.html'
    context_object_name = 'menus'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)  # no qa
        now = timezone.now().date()
        start = now - datetime.timedelta(days=now.weekday())
        data['start_date'] = start
        data['end_date'] = start + datetime.timedelta(days=6)
        return data

    def get_queryset(self):
        """This weeks menus"""
        now = timezone.now().date()
        start = now - datetime.timedelta(days=now.weekday())
        menus = []
        for num_day in range(7):
            menu = Menu.objects.filter(menu_date=start + datetime.timedelta(days=num_day))
            if menu.exists():
                menus.append((True, menu.first().id))
            else:
                menus.append((False, start + datetime.timedelta(days=num_day)))
        return menus

    def test_func(self):
        """Only Admin users can access this view"""
        return self.request.user.is_superuser
