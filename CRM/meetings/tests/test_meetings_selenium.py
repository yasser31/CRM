from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestMeeting(LiveServerTestCase):
    ''' selenium tests for meetings '''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.user = User.objects.create_user(username="username",
                                             password="password")

    def test_add_met_rep_sel(self):
        ''' test adding meeting report selenium '''
        self.driver.get("%s%s" % (self.live_server_url, "/"))
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        login = self.driver.find_element_by_class_name("login100-form-btn")
        username.send_keys("username")
        password.send_keys("password")
        login.click()
        self.driver.get("%s%s" % (self.live_server_url, "/create_meeting/"))
