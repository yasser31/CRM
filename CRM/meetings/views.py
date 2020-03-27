import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Meeting, SetMeeting
from .forms import MeetingForm, SetMeetingForm


@login_required(login_url='/')
def set_meeting(request):
    ''' set a mmeting view '''
    if request.method == "POST":
        form = SetMeetingForm(request.POST)
        if form.is_valid():
            try:
                SetMeeting.objects.get(
                    user__username=request.user.username,
                    date=request.POST["date"],
                    time=request.POST["time"])
            except SetMeeting.DoesNotExist:
                user = User.objects.get(username=request.user.username)
                place = form.cleaned_data["place"]
                date = form.cleaned_data["date"]
                time = form.cleaned_data["time"]
                contact = form.cleaned_data["contact"]
                SetMeeting.objects.create(
                    place=place, date=date, time=time, contact=contact,
                    user=user)
                return HttpResponseRedirect("/meeting_added/")
            else:
                context = {
                    "meeting": "exists"
                }
                return render(request, "contacts/already_exists.html",
                              context)
    else:
        form = SetMeetingForm(username=request.user.username)

    context = {
        "form": form
    }
    return render(request, "meetings/set_meeting.html", context)


@login_required(login_url='/')
def meetings(request):
    ''' list of contacts for meetings view '''
    nb_list = []
    contacts = Contact.objects.filter(user__username=request.user.username)
    if len(contacts) > 0:
        context = {
            "contacts": contacts,
            "count": nb_list
        }
        return render(request, "meetings/meeting.html", context)
    else:
        return render(request, "meetings/add_first.html")


@login_required(login_url='/')
def contact_meetings(request, contact_id):
    ''' list of meetings reports for a client view'''
    meetings = Meeting.objects.filter(user__username=request.user.username,
                                      contact__id=contact_id).order_by('-date')
    context = {
        "meetings": meetings
    }
    return render(request, "meetings/contact_meetings.html", context)


@login_required(login_url='/')
def meeting_details(request, meeting_id):
    ''' meeting report details '''
    meeting = Meeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meetings/meeting_detail.html", context)


@login_required(login_url='/')
def create_meeting(request):
    ''' creation of meeting report view '''
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
            return HttpResponseRedirect("/report_added/")
    context = {"form": MeetingForm(username=request.user.username)}
    return render(request, "meetings/create_meeting.html", context)


@login_required(login_url='/')
def meeting_information(request):
    ''' meetings with contacts information '''
    meetings = SetMeeting.objects.filter(user__username=request.user.username)
    context = {
        "meetings": meetings
    }

    return render(request, "meetings/meeting_information.html", context)


@login_required(login_url='/')
def meeting_notes(request, meeting_id):
    ''' meeting notes view, in case the user notes something for
       the next meeting he has with his conacts '''
    meeting = SetMeeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meetings/meeting_notes.html", context)


@login_required(login_url='/')
def dashboard_meeting_display(request):
    ''' display of next meeting view '''
    month = datetime.date.today().month
    year = datetime.date.today().year
    now = datetime.datetime.now().time()
    if month < 10:
        query_date = str(year) + '-' + '0' + str(month)
    else:
        query_date = str(year) + '-' + str(month)
    meetings = SetMeeting.objects.filter(date__startswith=query_date,
                                         user__username=request.user.username).order_by("date", "time")
    meeting = [{"date": meeting.date,
                "time": meeting.time,
                "place": meeting.place,
                "name": meeting.contact.name} for meeting in meetings
               if meeting.date >= datetime.date.today()
               and meeting.time >= now]
    data = {
        "meeting": meeting
    }
    return JsonResponse(data)


@login_required(login_url='/')
def meeting_added(request):
    ''' the last page redirected to when a meeting is added '''
    return render(request, "meetings/meeting_added.html")


@login_required(login_url='/')
def report_added(request):
    ''' the last page redirected to when a report is created '''
    return render(request, "meetings/report_added.html")


@login_required(login_url='/')
def edit_rep(request, rep_id):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.get(id=request.POST["contact"])
            met = Meeting.objects.get(id=rep_id)
            met.title = request.POST["title"]
            met.summary = request.POST["summary"]
            met.contact = contact
            met.save()
            return redirect("/report_edited/")
    else:
        met = Meeting.objects.get(id=rep_id)
        data = {
            "title": met.title,
            "summary": met.summary,
            "contact": met.contact
        }
        form = MeetingForm(data, username=request.user.username)
    context = {
        "form": form
    }
    return render(request, "meetings/edit_rep.html", context)


@login_required(login_url='/')
def edit_met(request, met_id):
    if request.method == 'POST':
        form = SetMeetingForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.get(id=request.POST["contact"])
            meeting = SetMeeting.objects.get(
                id=met_id)
            meeting.place = request.POST["place"]
            meeting.date = request.POST["date"]
            meeting.time = request.POST["time"]
            meeting.note = request.POST["note"]
            meeting.contact = contact
            meeting.save()
            return redirect("/meeting_edited/")
    else:
        met = SetMeeting.objects.get(id=met_id)
        data = {
            "place": met.place,
            "date": met.date,
            "time": met.time,
            "note": met.note,
            "contact": met.contact
        }
        form = SetMeetingForm(data, username=request.user.username)
    context = {
        "form": form
    }
    return render(request, "meetings/edit_met.html", context)


@login_required(login_url='/')
def report_edited(request):
    return render(request, "meetings/report_edited.html")


@login_required(login_url='/')
def meeting_edited(request):
    return render(request, "meetings/meeting_edited.html")


@login_required(login_url='/')
def delete_meeting(request, met_id):
    meeting = SetMeeting.objects.get(id=met_id)
    meeting.delete()
    return render(request, "meetings/meeting_deleted.html")


@login_required(login_url='/')
def delete_report(request, rep_id):
    rep = Meeting.objects.get(id=rep_id)
    rep.delete()
    return render(request, "meetings/report_deleted.html")
