"""Staff Urls."""

from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('menu/<uuid:menu_uuid>', views.menu, name='menu'),
    path('selection/new', views.selection_new, name='selection_new'),
]
