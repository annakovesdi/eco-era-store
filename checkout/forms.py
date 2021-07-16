from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'house_number', 'addition',
                  'postcode', 'city', 'country',)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    labels = {
        'full_name': 'Full Name',
        'email': 'Email Address',
        'phone_number': 'Phone Number',
        'street_address': 'Street Address',
        'house_number': 'House Number',
        'addition': 'Addition',
        'postcode': 'Postal Code',
        'city': 'City',
        'country': 'Country'
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            label = f'{labels[field]}*'
        else:
            label = labels[field]

    self.fields[field].widget.attrs['label'] = label
