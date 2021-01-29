from django import forms
from .models import Product, Category, Subcategory
from .widgets import CustomClearableFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # use_custom_control = True

    image1 = forms.ImageField(
        label='Image1', required=False, widget=CustomClearableFileInput)
    image2 = forms.ImageField(
        label='Image2', required=False, widget=CustomClearableFileInput)

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
        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     'category',
        #     'subcategory',
        #     'sku',
        #     'name',
        #     'quantity',
        #     'rating',
        #     'summary',
        #     'details',
        #     'has_sizes',
        #     'image1_url',
        #     Row(
        #         Column('image1', css_class='form-group col-6 mb-0'),
        #         Column('image2', css_class='form-group col-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded'
