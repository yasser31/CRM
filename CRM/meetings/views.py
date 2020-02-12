from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Meeting
from .forms import MeetingForm


def meetings(request):
    contacts = Contact.objects.all()
    context = {
        "contacts" : contacts
    }
    return render(request, "meeting.html", context)

def contact_meetings(request, contact_id):
    meetings = Meeting.objects.filter(user__username=request.user.username,
                                       contact_id=contact_id).order_by('-date')
    context = {
        "meetings" : meetings
    }
    return render(request, "contact_meetings.html", context)



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