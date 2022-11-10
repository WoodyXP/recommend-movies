from django.forms import ModelForm

from .models import Ebay_Product

class ProductForm(ModelForm):
    class Meta:
        model = Ebay_Product
        fields = ('title',)