from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestAdd(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/registration/")
        username = self.driver.find_element_by_name("username")
        email = self.driver.find_element_by_name("email")
        pass1 = self.driver.find_element_by_name("password1")
        pass2 = self.driver.find_element_by_name("password2")
        submit = self.driver.find_element_by_class_name("button")
        username.send_keys("username")
        email.send_keys("email@email.com")
        pass1.send_keys("Password@1")
        pass2.send_keys("Password@1")
        submit.send_keys(Keys.RETURN)

    def test_add_comp(self):
        self.driver.get("http://127.0.0.1:8000/add_company/")
        username = self.driver.find_element_by_name("username")
        username.send_keys("username")
        pass1 = self.driver.find_element_by_name("password")
        pass1.send_keys("Password@1")
        submit = self.driver.find_element_by_class_name("login100-form-btn")
        submit.send_keys(Keys.RETURN)
        el0 = self.driver.find_element_by_id("cp_name")
        el1 = self.driver.find_element_by_id("company_country")
        el2 = self.driver.find_element_by_id("company_city")
        el3 = self.driver.find_element_by_id("address")
        el4 = self.driver.find_element_by_id("submit")
        el0.send_keys("company")
        el1.send_keys("country")
        el2.send_keys("city")
        el3.send_keys("address")
        el4.send_keys(Keys.RETURN)
