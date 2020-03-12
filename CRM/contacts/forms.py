from django.forms import ModelForm, Textarea
from .models import Company, Departement, Contact


class NewCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['cp_name', 'address', 'company_country',
                  'company_city', 'field', 'description']
        widgets = {
            'cp_name': Textarea(attrs={'id': "cp_name"}),
            'address': Textarea(attrs={'id': "address"}),
            'company_country': Textarea(attrs={'id': "company_country"}),
            'company_city': Textarea(attrs={'id': "company_city"}),
        }


class NewDepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = ['dep_name']


class NewContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'city', 'phone_number', 'age', 'photo',
                  'function', 'description', 'twitter',
                  'facebook', 'linkedin', 'client']
