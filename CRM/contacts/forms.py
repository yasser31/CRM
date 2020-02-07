from django.forms import ModelForm
from .models import Contact


class NewContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'city', 'phone_number', 'age', 'photo', 
                  'function', 'company', 'description', 'twitter',
                  'facebook', 'linkedin', 'client']
