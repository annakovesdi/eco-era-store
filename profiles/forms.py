from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    labels = {
        'default_phone_number': 'Phone Number',
        'default_street_address': 'Street Address',
        'default_house_number': 'House Number',
        'default_addition': 'Addition',
        'default_postcode': 'Postal Code',
        'default_city': 'City',
        'default_country': 'Country'
    }

    self.fields['default_phone_number'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            label = f'{labels[field]}*'
        else:
            label = labels[field]

    self.fields[field].widget.attrs['label'] = label
