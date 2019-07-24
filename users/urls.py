"""User Object Urls."""

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.users, name='index'),
    path('<int:user_id>', views.show, name='show'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:user_id>/delete', views.destroy, name='destroy')
]
