from django.urls import path
from . import views


urlpatterns = [
    path("meetings/", views.meetings, name="meetings"),
    path("create_meeting/", views.create_meeting, name="create_meeting"),
    path("meetings/<int:contact_id>",
         views.contact_meetings, name="contact_meetings"),
    path("meeting_details/<int:meeting_id>",
         views.meeting_details, name="meeting_details"),
    path("set_meeting/", views.set_meeting, name="set_meeting"),
    path("meeting_information/", views.meeting_information,
         name="meeting_information"),
    path("meeting_notes/<int:meeting_id>",
         views.meeting_notes, name="meeting_notes"),
    path("meeting_display/", views.dashboard_meeting_display,
         name="meeting_display"),
    path("meeting_added/", views.meeting_added, name="meeting_added"),
    path("report_added/", views.report_added, name="report_added"),
]
