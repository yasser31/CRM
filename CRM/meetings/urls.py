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
    path("edit_rep/<int:rep_id>", views.edit_rep, name="edit_rep"),
    path("edit_met/<int:met_id>", views.edit_met, name="edit_met"),
    path("report_edited/", views.report_edited, name="report_edited"),
    path("meeting_edited/", views.meeting_edited, name="meeting_edited"),
    path("delete_meeting/<int:met_id>",
         views.delete_meeting, name="delete_meeting"),
    path("delete_report/<int:rep_id>", views.delete_report,
         name="delete_report"),
]
