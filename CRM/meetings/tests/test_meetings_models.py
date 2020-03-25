from django.test import TestCase
from meetings.models import Meeting, SetMeeting


class TestMeeting(TestCase):
    ''' test meeting report models '''
    def setUp(self):
        Meeting.objects.create(title="meeting", summary="this is ia summary")
        self.meeting = Meeting.objects.get(title="meeting")

    def test_create(self):
        ''' test create '''
        self.assertEqual(self.meeting.title, "meeting")

    def test_update(self):
        ''' test update '''
        self.meeting.title = "another title"
        self.meeting.save()
        self.assertEqual(self.meeting.title, "another title")

    def test_delete(self):
        ''' test delete '''
        self.meeting.delete()
        with self.assertRaises(Meeting.DoesNotExist):
            Meeting.objects.get(title="another title")


class TestSetMeeting(TestCase):
    ''' test seting meetings report '''

    def setUp(self):
        SetMeeting.objects.create(place="oran")
        self.setmeeting = SetMeeting.objects.get(place="oran")

    def test_create(self):
        ''' test create '''
        self.assertEqual(self.setmeeting.place, "oran")

    def test_update(self):
        ''' test update '''
        self.setmeeting.place = "alger"
        self.setmeeting.save()
        self.assertEqual(self.setmeeting.place, "alger")

    def test_delete(self):
        ''' test deletion '''
        self.setmeeting.delete()
        with self.assertRaises(SetMeeting.DoesNotExist):
            SetMeeting.objects.get(place="alger")
