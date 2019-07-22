import factory
import datetime

from django.utils import timezone

from lunch_poll.models import Menu


class MenuFactory(factory.DjangoModelFactory):
    """Define a dateless menu"""
    class Meta:
        model = Menu

    menu_intro = "Tester Menu"

class FutureMenuFactory(MenuFactory):
    """Define a future Menu"""
    menu_date = (timezone.now() + datetime.timedelta(days=1)).date()

class PresentMenuFactory(MenuFactory):
    """Define a future Menu"""
    menu_date = timezone.now().date()

class PastMenuFactory(MenuFactory):
    """Define a future Menu"""
    menu_date = (timezone.now() - datetime.timedelta(days=1)).date()
