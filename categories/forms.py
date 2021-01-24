from django import forms
from .models import Subcategory


class AddSubcategoryForm(forms.ModelForm):
    """Individual Add Form created to allow validation against exiting categories
    and prevent adding of categories with same category name """
    class Meta:
        model = Subcategory
        fields = ('name', 'friendly_name')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Please enter Database programmatical name here ...',
            'friendly_name': 'You may enter a more User-friendly name here...',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'subcategory-form-style-input'
            self.fields[field].label = False


class EditSubcategoryForm(forms.ModelForm):
    """Individual Edit Form created to allow validation against exiting categories
    and prevent adding of categories with same friendly name """
    class Meta:
        model = Subcategory
        fields = ('name', 'friendly_name')

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated labels, set name field
        to read only and set autofocus on friendly_name field"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'friendly_name': 'You may enter a more User-friendly name here...',
        }

        self.fields['friendly_name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'subcategory-form-style-input'
            self.fields[field].label = False
