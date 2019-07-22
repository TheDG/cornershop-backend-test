"""Lunch Poll Urls."""
from django.urls import path

from . import views

app_name = 'lunch_poll'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('menu', views.menu, name='menu'),
    path('menu/new', views.menu_new, name='menu_new'),

]
