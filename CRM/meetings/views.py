import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Meeting, SetMeeting
from .forms import MeetingForm, SetMeetingForm


@login_required(login_url='/')
def set_meeting(request):
    if request.method == "POST":
        form = SetMeetingForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            place = form.cleaned_data["place"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            contact = form.cleaned_data["contact"]
            SetMeeting.objects.create(
                place=place, date=date, time=time, contact=contact, user=user)
            return HttpResponseRedirect("/meeting_added/")
    else:
        form = SetMeetingForm()

    context = {
        "form": form
    }
    return render(request, "set_meeting.html", context)


@login_required(login_url='/')
def meetings(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "meeting.html", context)


@login_required(login_url='/')
def contact_meetings(request, contact_id):
    meetings = Meeting.objects.filter(user__username=request.user.username,
                                      contact_id=contact_id).order_by('-date')
    context = {
        "meetings": meetings
    }
    return render(request, "contact_meetings.html", context)


@login_required(login_url='/')
def meeting_details(request, meeting_id):

    meeting = Meeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meeting_detail.html", context)


@login_required(login_url='/')
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
    context = {"form": MeetingForm()}
    return render(request, "create_meeting.html", context)


@login_required(login_url='/')
def meeting_information(request):

    meetings = SetMeeting.objects.filter(user__username=request.user.username)
    context = {
        "meetings": meetings
    }

    return render(request, "meeting_information.html", context)


@login_required(login_url='/')
def meeting_notes(request, meeting_id):
    meeting = SetMeeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meeting_notes.html", context)


@login_required(login_url='/')
def dashboard_meeting_display(request):
    month = datetime.date.today().month
    year = datetime.date.today().year
    if month < 10:
        query_date = str(year) + '-' + '0' + str(month)
    else:
        query_date = str(year) + '-' + str(month)
    query_date = str(year) + '-' + '0' + str(month)
    meetings = SetMeeting.objects.filter(date__startswith=query_date)
    meeting = [{"date": meeting.date,
                "time": meeting.time,
                "place": meeting.place,
                "name": meeting.contact.name} for meeting in meetings
               if meeting.date > datetime.date.today()]
    data = {
        "meeting": meeting
    }
    return JsonResponse(data)


@login_required(login_url='/')
def meeting_added(request):
    return render(request, "meeting_added.html")
