from django.test import TestCase
from django.test import Client
from users import views, forms
from django.contrib.auth.models import User


class TestUserPost(TestCase):
    ''' test user post requests'''
    def setUp(self):
        self.client = Client()

    def test_register(self):
        ''' test regustration post request '''
        response = self.client.post("/registration/", {
            "username": "username",
            "email": "email@email.com",
            "password1": "Password@1",
            "password2": "Password@1"
        })
        user = User.objects.get(username="username")
        self.assertEqual(response.resolver_match.func, views.registration)
        self.assertEqual(user.username, "username")

    def test_login(self):
        ''' test login post request '''
        user = User.objects.create_user(username="username",
                                        password="Password@1")
        response = self.client.post("/", {
            "username": "username",
            "password": "Password@1",
        }, follow=True)
        self.assertTrue(response.redirect_chain[0][0], "/dashboard/")

    def test_change_password(self):
        ''' test change password post request '''
        user = User.objects.create_user(username="username",
                                        password="Password@1")
        self.client.force_login(user)
        response = self.client.post("/change_password/",
                                    {"old_password": "Password@1",
                                     "username": "username",
                                     "new_password": "Password@2",
                                     "confirm_password": "Password@2"},
                                    follow=True)
        user = User.objects.get(username="username")
        self.assertEqual(response.redirect_chain[0][0], "/change_done/")


class TestUserGet(TestCase):
    ''' test user get requests '''
    def setUp(self):
        self.client = Client()

    def test_get_reg(self):
        ''' test get registration page '''
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"])

    def test_get_login(self):
        ''' test get login page '''
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"])

    def test_get_change_done(self):
        ''' test the page redirected
        to when a password change
        has been done '''
        user = User.objects.create(username="username", password="password")
        self.client.force_login(user)
        response = self.client.get("/change_done/")
        self.assertEqual(response.status_code, 200)
