from django import forms


class NewContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone_number = forms.IntegerField(required=False)
    age = forms.IntegerField(required=False)
    photo = forms.ImageField(required=False)
    function = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    twitter = forms.URLField(max_length=128, required=False)
    facebook = forms.URLField(max_length=128, required=False)
    linkedin = forms.URLField(max_length=128, required=False)
    client = forms.BooleanField()