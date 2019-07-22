"""Lunch Poll Urls."""
from django.urls import path

from . import views

app_name = 'lunch_poll'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('menu', views.menu, name='menu'),
    path('menu/new', views.menu_new, name='menu_new'),
    path('menu/<int:menu_id>', views.menu_show, name='menu_show'),
    path('menu/<int:menu_id>/delete', views.menu_destroy, name='menu_destroy'),
]
