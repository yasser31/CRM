from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact


class Meetings(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(null=True)
    
