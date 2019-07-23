from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lunch_poll.models import Menu, Option

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    User.objects.all().delete()
    Menu.objects.all().delete()
    Option.objects.all().delete()

def create_users():
    admin = User.objects.create_user(first_name='Diego', last_name='Sinay',
                                     username="diegosinay", email='diegosinay@gmail.com',
                                     password='123123')
    admin.is_superuser = True
    admin.is_active = True
    admin.save()

    staff = User.objects.create_user(first_name='Diego', last_name='Sinay',
                                     username="staff", email='diegosinay@gmail.com',
                                     password='123123')
    staff.is_superuser = False
    staff.is_active = True
    staff.save()


def run_seed(mode):
    """ Seed database based on mode
    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_users()
