"""Staff views."""

from django.shortcuts import render, get_object_or_404
from lunch_poll.models import Menu, Selection


def menu(request, menu_uuid):
    """Staff show menu"""
    menu = get_object_or_404(Menu, uuid=menu_uuid)
    selection = Selection.objects.filter(selected_by=request.user, menu=menu)
    if not selection.exists():
        return render(request, 'staff/menu/show.html', {'menu': menu})
    return render(request, 'staff/selection/show.html',
                  {'menu': menu, 'selection': selection.first()})
