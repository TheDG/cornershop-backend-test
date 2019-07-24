"""Static Pages Urls."""

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.users, name='index'),
    path('<int:user_id>', views.show, name='show'),
    path('new', views.users, name='new'),
    path('<int:user_id>/delete', views.destroy, name='destroy')
]
