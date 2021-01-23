from django import forms
from .models import Subcategory


class SubcategoryForm(forms.ModelForm):
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
            'friendly_name': 'You May also enter a more User-friendly name here ...',
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
