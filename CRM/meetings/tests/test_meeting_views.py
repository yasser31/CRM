from django.test import TestCase
from meetings import views
from django.test import Client
from contacts.models import Contact
from meetings.models import Meeting, SetMeeting
from django.contrib.auth.models import User


class TestPostMetting(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)

    def test_create_meeting_rep(self):
        contact = Contact.objects.get(name="contact")
        response = self.client.post("/create_meeting/",
                                    {"title": "title",
                                     "summary": "summary",
                                     "contact": contact.id})
        meeting = Meeting.objects.get(title="title")
        self.assertEqual(meeting.title, "title")

    def test_set_meeting(self):
        contact = Contact.objects.get(name="contact")
        response = self.client.post("/set_meeting/", {
            "place": "oran",
            "date": "2020-03-20",
            "time": "10:20:15",
            "contact": contact.id
        })
        meeting = SetMeeting.objects.get(place="oran")
        self.assertEqual(meeting.place, "oran")
