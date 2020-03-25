from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Company(models.Model):
    ''' company model '''
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    cp_name = models.CharField(max_length=100, blank=False, default="")
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=256, blank=False, default="")
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    company_country = models.CharField(max_length=100, blank=False, default="")
    company_city = models.CharField(max_length=100, blank=False, default="")
    field = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    client = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cp_name


class Contact(models.Model):
    ''' contact model '''
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, default='', blank=False)
    country = models.CharField(max_length=100, default='', blank=False)
    city = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    age = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    dep_name = models.CharField(max_length=100, blank=True, null=True)
    function = models.CharField(max_length=100, default='', blank=False)
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
