from django.forms import ModelForm
from .models import Company, Departement, Contact


class NewCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['cp_name', 'address', 'country', 'city', 'field', 'description']


class NewDepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = ['dep_name']


class NewContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'city', 'phone_number', 'age', 'photo', 
                  'function', 'company', 'description', 'twitter',
                  'facebook', 'linkedin', 'client']
