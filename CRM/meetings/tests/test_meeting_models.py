from django.test import TestCase
from meetings.models import Meeting, SetMeeting


class TestMeeting(TestCase):

    def setUp(self):
        Meeting.objects.create(title="meeting", summary="this is ia summary")
        self.meeting = Meeting.objects.get(title="meeting")

    def test_create(self):
        self.assertEqual(self.meeting.title, "meeting")

    def test_update(self):
        self.meeting.title = "another title"
        self.meeting.save()
        self.assertEqual(self.meeting.title, "another title")

    def test_delete(self):
        self.meeting.delete()
        with self.assertRaises(Meeting.DoesNotExist):
            Meeting.objects.get(title="another title")


class TestSetMeeting(TestCase):
    def setUp(self):
        SetMeeting.objects.create(place="oran")
        self.setmeeting = SetMeeting.objects.get(place="oran")

    def test_create(self):
        self.assertEqual(self.setmeeting.place, "oran")

    def test_update(self):
        self.setmeeting.place = "alger"
        self.setmeeting.save()
        self.assertEqual(self.setmeeting.place, "alger")

    def test_delet(self):
        self.setmeeting.delete()
        with self.assertRaises(SetMeeting.DoesNotExist):
            SetMeeting.objects.get(place="alger")
