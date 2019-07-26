"""Test cases for lunch poll views"""

from django.test import TestCase
from django.urls import reverse

from ..factories.users import AdminFactory, StaffFactory


class LunchPollIndexViewTests(TestCase):
    """Test cases for lunch poll index"""
    def test_no_user(self):
        """ If no user is loged in, redirects to login page. """
        response = self.client.get(reverse('lunch_poll:index'))
        self.assertRedirects(response, "/accounts/login?redirect_to=/lunch_poll/",
                             status_code=302, fetch_redirect_response=False)

    def test_staff_user(self):
        """ If its a normal staff user, raises a 403 error. """
        client = self.client
        user = StaffFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:index'))
        self.assertEqual(response.status_code, 403)

    def test_admin_user(self):
        """ If its an admin user, redirects to lunch poll index. """
        client = self.client
        user = AdminFactory()
        client.force_login(user)
        response = client.get(reverse('lunch_poll:index'))
        self.assertEqual(response.status_code, 200)
        # TODO: update this test
        # self.assertQuerysetEqual(response.context['menus'], [])
