from django.test import TestCase			 # import default django test funtionality
from .models import Subcategory				 # import to facilitate CRUD operations
from django.contrib.auth.models import User  # Required to create SuperUser


# Subcategory Views validation

class TestSubcategoryViews(TestCase):

    def setUp(self):
        # create superuser to facilitate CRUD operations
        test_user1 = User.objects.create_superuser(
            username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_get_manage_categories_page(self):
        # login with superuser account
        # validate manage_categories page loads correctly
        # retrieve manage_categories page url
        # confirm http reponse is OK (200)
        # confirm template used
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/categories.html')

    def test_get_add_category_page(self):
        # login with superuser account
        # validate add_subcategory page loads correctly
        # retrieve add_subcategory page url
        # confirm http reponse is OK (200)
        # confirm template used
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/categories/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/add_subcategory.html')

    def test_get_edit_category_page(self):
        # login with superuser account
        # create test subcategory
        # validate edit_subcategory page loads correctly
        # retrieve edit_subcategory page url
        # confirm http reponse is OK (200)
        # confirm template used
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(name='test_subcategory_1')
        response = self.client.get(f'/categories/edit/{subcategory.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/edit_subcategory.html')

    def test_delete_sucategory_operation(self):
        # login with superuser account
        # create test subcategory
        # validate delete item operation
        # retrieve delete url with created test subcategory
        # confirm redirects to manage_categories page
        # create variable with all objects created
        # confirm variable length is zero (i.e. no subcategories exist)
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(name='test_subcategory_1')
        response = self.client.get(f'/categories/delete/{subcategory.id}/')
        self.assertRedirects(response, '/categories/')
        existing_subcategories = Subcategory.objects.filter(id=subcategory.id)
        self.assertEqual(len(existing_subcategories), 0)

    def test_post_subcategory_update(self):
        # login with superuser account
        # validate item update operation
        # create new item
        # post update of name and friendly
        # note requires both fields to update correctly
        # confirm redirects to manage categories page
        # confirm response status code is 302 (found)
        # assign update info to new variable
        # confirm friendly name value is as it should be
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        subcategory = Subcategory.objects.create(
            name='test_subcategory_1', friendly_name='test')
        response = self.client.post(f'/categories/edit/{subcategory.id}/', {
                                    'name': 'test_subcategory_1', 'friendly_name': 'Updated Friendly Name'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/categories/')
        updated_subcategory = Subcategory.objects.get(id=subcategory.id)
        self.assertEqual(updated_subcategory.friendly_name,
                         'Updated Friendly Name')

    def test_post_subcategory_add(self):
        # login with superuser account
        # validate add subcategory operation
        # submit post to add subcategory test_added_subcategory_1
        # confirm redirects to manage categories page
        # confirm single instance created in database
        # assign update info to new variable
        # confirm name string is as it should be
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post(
            '/categories/add/', {'name': 'test_added_subcategory_1'})
        self.assertRedirects(response, "/categories/")
        self.assertEqual(Subcategory.objects.count(), 1)
        new_subcategory = Subcategory.objects.get()
        self.assertEqual(new_subcategory.name,
                         'test_added_subcategory_1')
