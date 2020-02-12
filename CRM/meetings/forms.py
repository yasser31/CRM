from django import forms
from contacts.models import Contact
from .models import Meeting


class MeetingForm(forms.Form):
    title = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())