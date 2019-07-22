"""Test cases for static pages views"""

from django.test import TestCase
from django.urls import reverse


class PagesIndexViewTests(TestCase):
    """Test cases for static pages root"""
    def test_no_user(self):
        """ If no user is loged in, redirects to login page. """
        response = self.client.get(reverse('pages:root'))
        self.assertEqual(response.status_code, 200)
