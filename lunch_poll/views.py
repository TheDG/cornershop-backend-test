"""Lunch Poll views / router."""

from django.views import generic


class IndexView(generic.ListView):
    """Admin main page"""
    template_name = 'lunch_poll/index.html'

    def get_queryset(self):
        """Meanwhile return nothing"""
        return []
