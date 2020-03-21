from django.test import TestCase
from meetings import views
from django.test import Client
from contacts.models import Contact
from meetings.models import Meeting, SetMeeting
from django.contrib.auth.models import User


class TestPostMetting(TestCase):
    ''' test post requests meetings'''

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)

    def test_create_meeting_rep(self):
        ''' test create met rep request '''
        contact = Contact.objects.get(name="contact")
        response = self.client.post("/create_meeting/",
                                    {"title": "title",
                                     "summary": "summary",
                                     "contact": contact.id})
        meeting = Meeting.objects.get(title="title")
        self.assertEqual(meeting.title, "title")

    def test_set_meeting(self):
        ''' test set meeting rep request '''
        contact = Contact.objects.get(name="contact")
        response = self.client.post("/set_meeting/", {
            "place": "oran",
            "date": "2020-03-20",
            "time": "10:20:15",
            "contact": contact.id
        })
        meeting = SetMeeting.objects.get(place="oran")
        self.assertEqual(meeting.place, "oran")


class TestGetMeeting(TestCase):
    ''' test get requests '''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="yasser",
                                             password="secret")
        self.client.force_login(self.user)
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)
        self.contact = Contact.objects.get(name="contact")
        Meeting.objects.create(title="title",
                               summary="summary",
                               contact=self.contact,
                               user=self.user)

        SetMeeting.objects.create(place="oran",
                                  date="2020-03-31",
                                  time="10:20:15",
                                  contact=self.contact,
                                  user=self.user)

    def test_met_cl_lst(self):
        ''' test meetings client list '''
        response = self.client.get("/meetings/")
        self.assertEqual(response.status_code, 200)

    def test_contact_meetings_rep(self):
        ''' test meetings for a client '''
        response = self.client.get(f"/meetings/{self.contact.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["meetings"][0].title, "title")

    def test_meeting_information(self):
        ''' test information about a meeting '''
        response = self.client.get("/meeting_information/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["meetings"][0].place, "oran")

    def test_meeting_notes(self):
        ''' test meeting notes '''
        meeting = SetMeeting.objects.get(place="oran")
        response = self.client.get(f"/meeting_notes/{meeting.id}")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_met_disp(self):
        ''' test the display of the meetings in dashboard '''
        response = self.client.get("/meeting_display/")
        data = response.json()
        self.assertEqual(data["meeting"][0]["place"], "oran")

    def test_meeting_added(self):
        ''' test final page redirected to when a meeting is added '''
        response = self.client.get("/meeting_added/")
        self.assertEqual(response.status_code, 200)

    def test_meeting_details(self):
        ''' test meeting report details '''
        meeting = Meeting.objects.get(title="title")
        response = self.client.get(f"/meeting_details/{meeting.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["meeting"].title, "title")
