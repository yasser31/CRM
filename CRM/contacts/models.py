from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Company(models.Model):
    cp_name = models.CharField(max_length=100, blank=False, default="")
    address = models.TextField()
    company_country = models.CharField(max_length=100, blank=False, default="")
    company_city = models.CharField(max_length=100, blank=False, default="")
    field = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Departement(models.Model):
    dep_name = models.CharField(max_length=100, blank=True, null=True)
    cp = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    country = models.CharField(max_length=100, default='', blank=False)
    city = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    age = models.IntegerField(null=True)
    photo = models.ImageField(blank=True, upload_to='media')
    function = models.CharField(max_length=100, default='', blank=False)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.DO_NOTHING, null=True)
    description = models.TextField(blank=True)
    twitter = models.URLField(max_length=128, blank=True, unique=True,  null=True)
    facebook = models.URLField(max_length=128, blank=True, unique=True, null=True)
    linkedin = models.URLField(max_length=128, blank=True, unique=True, null=True)
    client = models.BooleanField(null=False, default='false')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    