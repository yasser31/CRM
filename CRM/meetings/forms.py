from django import forms
from contacts.models import Contact
from .models import Meeting, SetMeeting


class MeetingForm(forms.Form):
    title = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())


class SetMeetingForm(forms.ModelForm):
    class Meta:
        model = SetMeeting
        fields = ["date", "contact"]
        widgets = {
            "date": forms.TextInput(attrs={"class" : "datepicker"}),
        }
    
    def __init__(self):
        super(SetMeetingForm, self).__init__()
        self.fields["contact"].queryset = Contact.objects.all()