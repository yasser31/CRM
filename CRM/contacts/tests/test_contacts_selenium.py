from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestAdd(LiveServerTestCase):
    ''' Selenium tests'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.user = User.objects.create_user(username="username",
                                             password="password")

    def test_contact(self):
        ''' test adding a company departement contact'''
        self.driver.get("%s%s" % (self.live_server_url, "/"))
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        login = self.driver.find_element_by_class_name("login100-form-btn")
        username.send_keys("username")
        password.send_keys("password")
        login.click()
        self.driver.get("%s%s" % (self.live_server_url, "/add_company/"))
        el0 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "cp_name"))
        )
        el1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "address"))
        )
        el2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company_country"))
        )
        el3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company_city"))
        )
        el0.send_keys("company")
        el1.send_keys("address")
        el2.send_keys("country")
        el3.send_keys("city")
        add_departement = self.driver.find_element_by_id("submit")
        add_departement.click()
        dep_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dep_name"))
        )
        dep_name.send_keys("dep_name")
        add_contact = self.driver.find_element_by_id("submit")
        add_contact.click()
        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "country"))
        )
        city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "city"))
        )
        age = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "age"))
        )
        function = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "function"))
        )
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "user"))
        )
        for option in user.find_elements_by_tag_name('option'):
            if option.text == self.user.username:
                option.click()
                break
        name.send_keys("name")
        email.send_keys("email@email.com")
        country.send_keys("country")
        city.send_keys("city")
        age.send_keys(29)
        function.send_keys("function")
        finish = self.driver.find_element_by_id("submit")
        finish.click()
        self.assertTrue("Contact added thanks" in self.driver.page_source)
