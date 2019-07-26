"""User Object views."""

import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
import slack
from .forms import UserForm


def use_paginator(objects, request):
    """Auxiliar method to dry up code."""
    paginator = Paginator(objects, 10)
    page = request.GET.get('page')
    return paginator.get_page(page)


@login_required(login_url='/accounts/login/')
def users(request):
    """User index controller"""
    display_users = User.objects.all().order_by('last_name')
    return render(request, 'users/index.html', {'users': use_paginator(display_users, request)})


@login_required(login_url='/accounts/login/')
@permission_required('users.view_user')
def show(request, user_id):
    """Get user with id and show"""
    display_user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/show.html', {'user': display_user})


@login_required(login_url='/accounts/login/')
@permission_required('users.add_user')
def new(request):
    """Render new user form"""
    form = UserForm()
    return render(request, 'users/new.html', {'form': form})


@login_required(login_url='/accounts/login/')
@permission_required('users.add_user')
def create(request):
    """Create new user from form"""
    form = UserForm(request.POST)
    password = User.objects.make_random_password()
    form.password = password
    if form.is_valid():
        form.save()
        messages.success(request, "Succesfully created user")
        return redirect(reverse('users:index'))
    return render(request, 'users/new.html', {'form': form})


@login_required(login_url='/accounts/login/')
@permission_required('users.delete_user')
def destroy(request, user_id):
    """Delete user"""
    selected_user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        if not selected_user.is_superuser:
            messages.success(
                request, f"Succesfully deleted user {selected_user.username}")
            selected_user.delete()
        else:
            messages.error(request, "Can't delete an admin user")
    display_users = User.objects.all().order_by('last_name')
    return render(request, 'users/index.html', {'users': use_paginator(display_users, request)})


@login_required(login_url='/accounts/login/')
@permission_required('users.add_user')
def massive_upload(request):
    """Create Users from Slack app. TODO: refactor move logic to User Model"""
    client = slack.WebClient(token=os.getenv("SLACK_API_TOKEN"))
    response = client.users_list()
    if response['ok']:
        for member in response['members']:
            if member.get('name', '') == 'slackbot' or member['is_bot'] is True:
                continue
            aux_name = member.get('real_name', 'Jane')
            User.objects.get_or_create(
                username=member['id'],
                defaults={
                    'first_name': member['profile'].get('first_name', aux_name),
                    'last_name': member['profile'].get('last_name', 'Doe'),
                    'email': member['profile'].get('email', 'No Email')
                })
        messages.success(request, "Sucesfully mass loaded users")
    else:
        messages.error(request, "Error mass loading users")
    return redirect(reverse('users:new'))
