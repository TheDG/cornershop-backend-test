"""Test cases for lunch poll menu views"""

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from lunch_poll.models import Menu
from ..factories.menus import FutureMenuFactory
from ..factories.users import AdminFactory, StaffFactory


class MenuNew(TestCase):
    """Test cases for lunch poll menu new"""

    def test_staff_user(self):
        """ If its a normal staff user, raises a 403 error. """
        client = self.client
        user = StaffFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:menu_new'))
        self.assertEqual(response.status_code, 302)

    def test_admin_user(self):
        """ If its an admin user, redirects to lunch poll index. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:menu_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


class MenuShow(TestCase):
    """Test cases for lunch poll menu show action"""

    def test_staff_user(self):
        """ If its a normal staff user, raises a 403 error. """
        client = self.client
        user = StaffFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:menu'))
        self.assertEqual(response.status_code, 302)

    def test_admin_user_with_correct_input(self):
        """ If its an admin user with incorrect menu id, raises 402. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        response = client.get(
            reverse('lunch_poll:menu_show', kwargs={'menu_id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_admin_user_with_menu(self):
        """ If its an admin user with incorrect menu id, raises 402. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        menu = FutureMenuFactory()
        response = client.get(
            reverse('lunch_poll:menu_show', kwargs={'menu_id': menu.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['menu'], menu)


class MenuPost(TestCase):
    """Test cases for lunch poll menu post action"""

    def test_staff_user(self):
        """ If its a normal staff user, raises a 403 error. """
        client = self.client
        user = StaffFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:menu'))
        self.assertEqual(response.status_code, 302)

    def test_admin_user_with_correct_input(self):
        """ If its an admin user with correct input, creates menu. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        self.assertEqual(0, Menu.objects.all().count())
        client.post(reverse('lunch_poll:menu'),
                    {'menu_date': timezone.now().date(), 'menu_intro': 'Tester'})
        self.assertEqual(1, Menu.objects.all().count())

    def test_admin_user_with_incorrect_input(self):
        """ If its an admin user with incorrect input, does not creates menu. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        self.assertEqual(0, Menu.objects.all().count())
        response = client.post(reverse('lunch_poll:menu'), {})
        self.assertEqual(0, Menu.objects.all().count())
        self.assertFormError(response, 'form', 'menu_date',
                             'This field is required.')
