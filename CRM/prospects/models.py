from django.db import models


class Prospects:
    name = models.CharField(max_length=100, default='', blank=False)
    age = models.IntegerField(null=True)
    photo = models.ImageField(null=True, upload_to='/media/')
    function = models.CharField(max_length=100, default='', blank=False)
    company = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(blank=True, null=True)
    client = models.BooleanField(null=False, default='false')

    def __str__(self):
        return self.name