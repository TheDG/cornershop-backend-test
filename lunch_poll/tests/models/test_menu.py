
from django.test import TestCase
from ..factories.menus import FutureMenuFactory, PresentMenuFactory, PastMenuFactory


class MenuActiveTests(TestCase):

    def test_menu_in_the_future(self):
        """is_active() returns True for menus in future days"""
        future_menu = FutureMenuFactory()
        self.assertIs(future_menu.is_active(), True)

    def test_menu_in_the_present(self):
        """is_active() returns True for menus in present day"""
        present_menu = PresentMenuFactory()
        self.assertIs(present_menu.is_active(), True)

    def test_menu_in_the_past(self):
        """is_active() returns False for menus in past days"""
        past_menu = PastMenuFactory()
        self.assertIs(past_menu.is_active(), False)


class MenuCreateTests(TestCase):

    def test_menu_in_with_same_date(self):
        """if menu with date existes, raises error"""
        FutureMenuFactory()
        with self.assertRaises(Exception):
            FutureMenuFactory()
