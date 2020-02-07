from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.BigIntegerField(null=True)
    age = models.IntegerField(null=True)
    photo = models.ImageField(blank=True, upload_to='media')
    function = models.CharField(max_length=100, default='', blank=False)
    company = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(blank=True)
    twitter = models.URLField(max_length=128, blank=True, unique=True)
    facebook = models.URLField(max_length=128, blank=True, unique=True)
    linkedin = models.URLField(max_length=128, blank=True, unique=True)
    client = models.BooleanField(null=False, default='false')

    def __str__(self):
        return self.name