from django.urls import path
from . import views


urlpatterns = [
    path("meetings/", views.meetings, name="meetings"),
    path("create_meeting/", views.create_meeting, name="create_meeting"),
    path("meetings/<int:contact_id>", views.contact_meetings, name="contact_meetings")
]