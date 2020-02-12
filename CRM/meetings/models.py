from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact


class Meeting(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True, default='')
    summary = models.TextField(null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title