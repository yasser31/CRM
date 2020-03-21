from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact


class Meeting(models.Model):
    ''' meeting report model '''
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True, default='')
    summary = models.TextField(null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title


class SetMeeting(models.Model):
    ''' setting a meeting model '''
    place = models.CharField(null=True, blank=True, max_length=100)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    note = models.TextField(null=True, blank=True)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)
