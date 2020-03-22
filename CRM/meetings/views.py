import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
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
    ''' list of contacts for meetings view '''
    contacts = Contact.objects.all()
    if len(contacts) > 0:
        context = {
            "contacts": contacts
        }
        return render(request, "meeting.html", context)
    else:
        return HttpResponse("add contacts and reports first")


@login_required(login_url='/')
def contact_meetings(request, contact_id):
    ''' list of meetings reports for a client view'''
    meetings = Meeting.objects.filter(user__username=request.user.username,
                                      contact__id=contact_id).order_by('-date')
    context = {
        "meetings": meetings
    }
    return render(request, "contact_meetings.html", context)


@login_required(login_url='/')
def meeting_details(request, meeting_id):
    ''' meeting report details '''
    meeting = Meeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meeting_detail.html", context)


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
    context = {"form": MeetingForm()}
    return render(request, "create_meeting.html", context)


@login_required(login_url='/')
def meeting_information(request):
    ''' meetings with contacts information '''
    meetings = SetMeeting.objects.filter(user__username=request.user.username)
    context = {
        "meetings": meetings
    }

    return render(request, "meeting_information.html", context)


@login_required(login_url='/')
def meeting_notes(request, meeting_id):
    ''' meeting notes view, in case the user notes something for
       the next meeting he has with his conacts '''
    meeting = SetMeeting.objects.get(id=meeting_id)
    context = {
        "meeting": meeting
    }

    return render(request, "meeting_notes.html", context)


@login_required(login_url='/')
def dashboard_meeting_display(request):
    ''' display of next meeting view '''
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
    ''' the last page redirected to when a meeting is added '''
    return render(request, "meeting_added.html")


@login_required(login_url='/')
def report_added(request):
    ''' the last page redirected to when a report is created '''
    return render(request, "report_added.html")


@login_required(login_url='/')
def edit_rep_get(request, rep_id):
    met = Meeting.objects.get(id=rep_id)
    request.session['met_id'] = rep_id
    data = {
        "title": met.title,
        "summary": met.summary,
        "contact": met.contact
    }
    form = MeetingForm(data)
    context = {
        "form": form
    }
    return render(request, "edit_rep.html", context)


@login_required(login_url='/')
def edit_rep_post(request):
    form = MeetingForm(request.POST)
    if form.is_valid():
        met_id = request.session.get("met_id")
        contact = Contact.objects.get(id=request.POST["contact"])
        met = Meeting.objects.get(id=met_id)
        met.title = request.POST["title"]
        met.summary = request.POST["summary"]
        met.contact = contact
        met.save()
        return HttpResponse("report edited thanks")
    else:
        context = {
            "form": form
        }
    return render(request, "edit_rep.html", context)


@login_required(login_url='/')
def edit_met_get(request, met_id):
    met = SetMeeting.objects.get(id=met_id)
    request.session["meeting_id"] = met_id
    data = {
        "place": met.place,
        "date": met.date,
        "time": met.time,
        "note": met.note,
        "contact": met.contact
    }
    form = SetMeetingForm(data)
    context = {
        "form": form
    }
    return render(request, "edit_met.html", context)


@login_required(login_url='/')
def edit_met_post(request):
    form = SetMeetingForm(request.POST)
    if form.is_valid():
        contact = Contact.objects.get(id=request.POST["contact"])
        meeting = SetMeeting.objects.get(id=request.session.get("meeting_id"))
        meeting.place = request.POST["place"]
        meeting.date = request.POST["date"]
        meeting.time = request.POST["time"]
        meeting.note = request.POST["note"]
        meeting.contact = contact
        meeting.save()
        return HttpResponse(" meeting edited thanks ")
    else:
        context = {
             "form": form
        }
        return render(request, "edit_met.html", context)
