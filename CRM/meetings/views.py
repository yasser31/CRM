from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Meetings
from .forms import MeetingForm


def meetings(request):
    meetings = Meetings.objects.filter(user=request.user.username)
    context = {
        "meetings" : meetings
    }
    return render(request, "meetings.html", context)


def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.user.username)
            contact = Contact.objects.filter(user_username=request.user.username)
            meeting = Meetings.objects.get(title=request.POST["title"])
            meeting.user = user
            meetings.contact = contact
            return HttpResponseRedirect("/thanks/")
    return render(request, "create_meeting.html")