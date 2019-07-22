import factory

from django.contrib.auth.models import User


class AdminFactory(factory.DjangoModelFactory):
    """
        Define a Admin / Superuser
    """
    class Meta:
        model = User

    first_name = 'Diego'
    last_name = 'Sinay'
    username = "diegosinay"
    email = 'diegosinay@gmail.com'
    password = '123123'
    is_superuser = True
    is_active = True


class StaffFactory(factory.DjangoModelFactory):
    """
        Define a Employee / Staff user
    """
    class Meta:
        model = User

    first_name = 'Ricky'
    last_name = 'Staffer'
    username = "staffer"
    email = 'staff@gmail.com'
    password = '123123'
    is_superuser = False
    is_active = True
