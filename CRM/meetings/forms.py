import datetime
import pytz
from django import forms
from contacts.models import Contact
from .models import Meeting, SetMeeting
from django.contrib.auth.models import User


class MeetingForm(forms.Form):
    ''' meeting report form '''
    title = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    contact = forms.ModelChoiceField(queryset=Contact.objects.filter())

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super(MeetingForm, self).__init__(*args, **kwargs)
        if username:
            self.fields["contact"].queryset = Contact.objects.filter(
                user__username=username)


class SetMeetingForm(forms.Form):
    ''' set a meeting report '''
    place = forms.CharField(max_length=100, required=False)
    date = forms.DateField(widget=forms.DateInput(
        attrs={"type": "date"}, format="%Y-%m-%d"))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())
    note = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super(SetMeetingForm, self).__init__(*args, **kwargs)
        if username:
            self.fields["contact"].queryset = Contact.objects.filter(
                user__username=username)

    def clean_date(self):
        self.date = self.cleaned_data["date"]
        now = datetime.datetime.now().time()
        if self.date < datetime.date.today():
            raise forms.ValidationError("please select a futur date")
        return self.date

    def clean_time(self):
        tz_str = "Africa/Algiers"
        tz = pytz.timezone(tz_str)
        time = self.cleaned_data["time"]
        now = datetime.datetime.now(tz).time()
        if self.date == datetime.date.today() and time < now:
            raise forms.ValidationError("please select a futur time")
        return time
