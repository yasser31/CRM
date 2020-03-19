from django import forms
from contacts.models import Contact
from .models import Meeting, SetMeeting


class MeetingForm(forms.Form):
    ''' meeting report form '''
    title = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())


class SetMeetingForm(forms.Form):
    ''' set a meeting report '''
    place = forms.CharField(max_length=100, required=False)
    date = forms.DateField(widget=forms.DateInput(
        attrs={"type": "date"}, format="%Y-%m-%d"))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())
    note = forms.CharField(widget=forms.Textarea, required=False)
