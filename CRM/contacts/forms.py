from django.forms import ModelForm
from .models import Company, Departement, Contact
from django.contrib.auth.models import User


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

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super(NewContactForm, self).__init__(*args, **kwargs)
        if username:
            self.fields["user"].queryset = User.objects.filter(
                username=username)
