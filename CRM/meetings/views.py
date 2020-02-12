from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Meeting
from .forms import MeetingForm


def meetings(request):
    meetings = Meeting.objects.filter(user=request.user.username)
    context = {
        "meetings" : meetings
    }
    return render(request, "meetings.html", context)


def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            contact_id = request.POST["contact"]
            contact = Contact.objects.get(id=contact_id)
            title = form.cleaned_data["title"]
            summary = form.cleaned_data["summary"]
            new_meeting = Meeting.objects.create(title=title, 
                                                  contact=contact,
                                                  summary=summary,
                                                  user=user)
            new_meeting.save()
            return HttpResponseRedirect("/thanks/")
    context = {"form" : MeetingForm()}
    return render(request, "create_meeting.html", context)