from django.test import TestCase			# import default django test funtionality
from .forms import AddSubcategoryForm		# import AddSubcategoryForm from .forms


# Forms Test Cases
# pass in Django Test functionality

class TestAddSubcategoryForm(TestCase):

    def test_category_name_is_required(self):
        # validate name field is required
        # instantiate without name value
        # test form is invalid
        # confirm error on name field
        # test error message as expected
        form = AddSubcategoryForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_friendly_name_not_required(self):
        # validate friendly_name field is not required
        # instantiate form without friendly_name
        # test form is valid
        form = AddSubcategoryForm({'name': 'test_add_category_form'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # only fields displayed in form are the name & friendly_name
        # instantiate empty form
        # form.meta.fields attribute = list with name & friendly_name in it.
        # confirm form meta contains only 2 fields specified
        form = AddSubcategoryForm()
        self.assertTrue(form.Meta.fields, ('name', 'friendly_name'))
        self.assertNotEqual(form.Meta.fields, ('name', 'friendly_name', 'new'))
