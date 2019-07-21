"""Static Pages views."""

from django.shortcuts import render


def index(request):
    """Project Landing page"""
    return render(request, 'pages/index.html')
