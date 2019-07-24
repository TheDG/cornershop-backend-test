"""User views."""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages


@login_required(login_url='/accounts/login/')
@permission_required('users.add_user')
def users(request):
    """User index controller"""
    users = User.objects.all().order_by('last_name')
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'users/index.html', {'users': users})


@login_required(login_url='/accounts/login/')
@permission_required('users.view_user')
def show(request, user_id):
    """Get user with id and show"""
    display_user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/show.html', {'user': display_user})


@login_required(login_url='/accounts/login/')
@permission_required('users.delete_user')
def destroy(request, user_id):
    """Delete user"""
    selected_user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        if not selected_user.is_superuser:
            messages.success(request, f"Succesfully deleted user {selected_user.username}")
            selected_user.delete()
        else:
            messages.error(request, "Can't delete an admin user")
    users = User.objects.all().order_by('last_name')
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'users/index.html', {'users': users})
