from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __innit__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = names
