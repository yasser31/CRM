from django.forms import ModelForm
from .models import Company, Departement, Contact


class NewCompanyForm(ModelForm):
    ''' add company '''
    class Meta:
        model = Company
        fields = ['cp_name', 'address', 'company_country',
                  'company_city', 'field', 'description']


class NewDepartementForm(ModelForm):
    ''' add departement '''
    class Meta:
        model = Departement
        fields = ['dep_name']


class NewContactForm(ModelForm):
    ''' add contact'''
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'city', 'phone_number', 'age',
                  'function', 'description', 'twitter',
                  'facebook', 'linkedin', 'client', "user"]
