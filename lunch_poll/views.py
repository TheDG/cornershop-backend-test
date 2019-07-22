"""Lunch Poll views / router."""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """Admin main page"""
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    template_name = 'lunch_poll/index.html'
    permission_required = 'polls.can_vote'

    def get_queryset(self):
        """Meanwhile return nothing"""
        return []

    def test_func(self):
        """Only Admin users can access this view"""
        return self.request.user.is_superuser
