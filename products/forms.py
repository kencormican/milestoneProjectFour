from django import forms
from .models import Product, Category, Subcategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        cat_friendly_names = [(
            cat.id, cat.get_friendly_name()) for cat in categories]
        scat_friendly_names = [(
            scat.id, scat.get_friendly_name()) for scat in subcategories]

        self.fields['category'].choices = cat_friendly_names
        self.fields['subcategory'].choices = scat_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded'


