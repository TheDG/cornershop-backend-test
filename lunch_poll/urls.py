"""Lunch Poll Urls."""
from django.urls import path

from . import views

app_name = 'lunch_poll'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('menu', views.menu, name='menu'),
    path('menu/new', views.MenuCreate.as_view(), name='menu_new'),
    path('menu/new?<menu_date>', views.menu_new_with_date, name='menu_new_with_date'),
    path('menu/<int:menu_id>', views.menu_show, name='menu_show'),
    path('menu/<int:menu_id>/delete', views.menu_destroy, name='menu_destroy'),
]
