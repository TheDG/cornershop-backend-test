from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

#from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'lunch_poll/index.html'

    def get_queryset(self):
        """Meanwhile return nothing"""
        return []
