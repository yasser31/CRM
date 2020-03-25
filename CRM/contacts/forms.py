from django.forms import ModelForm
from .models import Company, Contact
from django.contrib.auth.models import User


class NewCompanyForm(ModelForm):
    ''' add company '''
    class Meta:
        model = Company
        fields = ['cp_name', 'address', 'email', 'phone_number',
                  'company_country',
                  'company_city', 'field', 'description', "client"]


class NewContactForm(ModelForm):
    ''' add contact'''
    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'city', 'phone_number', 'age',
                  'photo', 'function', 'dep_name', "user", "company"]

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        company_id = kwargs.pop('company_id', None)
        super(NewContactForm, self).__init__(*args, **kwargs)
        if username:
            self.fields["user"].queryset = User.objects.filter(
                username=username)
            self.fields["company"].queryset = Company.objects.filter(
                user__username=username, id=company_id)
