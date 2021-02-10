from django.test import TestCase			 # import default django test funtionality
from .models import Subcategory, Category    # import to facilitate CRUD operations
from django.contrib.auth.models import User  # Required to create SuperUser


# Models validation

class TestSubcategyModels(TestCase):

    def setUp(self):
        # create superuser to facilitate CRUD operations
        test_user1 = User.objects.create_superuser(
            username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_new_defaults_to_true(self):
        # login with superuser account
        # validate model sets new field to true by default
        # create test subcategory without explicitly configuring new field
        # confirm variable new field is true
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(name='test_subcategory_1')
        self.assertTrue(subcategory.new)

    def test_subcategory_string_method_returns_name(self):
        # login with superuser account
        # confirm name returned when render subcategory as a string
        # validate string value
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(
            name='test_subcategory_1', friendly_name='Test Subcategory 1')
        self.assertEqual(str(subcategory), 'test_subcategory_1')

    def test_subcategory_get_friendly_name_method_returns_friendly_name(self):
        # login with superuser account
        # confirm friendly_name returned when get_friendly_name() method run
        # validate friendly name
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(
            name='test_subcategory_1', friendly_name='Test Subcategory 1')
        self.assertEqual(subcategory.get_friendly_name(), 'Test Subcategory 1')

    def test_category_string_method_returns_name(self):
        # login with superuser account
        # confirm name returned when render category as a string
        # validate string value
        # validate friendly name
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        category = Category.objects.create(
            name='test_category_1', friendly_name='Test Category 1')
        self.assertEqual(str(category), 'test_category_1')

    def test_category_get_friendly_name_method_returns_friendly_name(self):
        # login with superuser account
        # confirm friendly_name returned when get_friendly_name() method run
        # validate friendly name
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        category = Category.objects.create(
            name='test_category_1', friendly_name='Test Category 1')
        self.assertEqual(category.get_friendly_name(), 'Test Category 1')
