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

    def __str__(self):
        return self.cp_name


class Departement(models.Model):
    dep_name = models.CharField(max_length=100, blank=True, null=True)
    cp = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dep_name


class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, default='', blank=False)
    country = models.CharField(max_length=100, default='', blank=False)
    city = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    age = models.IntegerField(null=True, blank=True)
    function = models.CharField(max_length=100, default='', blank=False)
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True)
    departement = models.ForeignKey(
        Departement, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    twitter = models.URLField(
        max_length=128, blank=True, unique=True,  null=True)
    facebook = models.URLField(
        max_length=128, blank=True, unique=True, null=True)
    linkedin = models.URLField(
        max_length=128, blank=True, unique=True, null=True)
    client = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
