from django import forms

from .models import Products,Category,Tags

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'