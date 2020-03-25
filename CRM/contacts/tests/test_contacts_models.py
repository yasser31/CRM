from django.test import TestCase
from ..models import Company, Contact


class TestCompany(TestCase):
    ''' test compay model '''

    def setUp(self):
        Company.objects.create(cp_name="company", company_country="Algeria",
                               company_city="Oran", address="address")
        self.company = Company.objects.get(cp_name="company")

    def test_create(self):
        ''' test the creation of the model'''
        self.assertEqual(self.company.cp_name, "company")

    def test_update(self):
        ''' test the update of the model'''
        self.company.cp_name = "another_name"
        self.company.save()
        self.assertEqual(self.company.cp_name, "another_name")

    def test_delete(self):
        ''' test the deletion of the model'''
        self.company.delete()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(cp_name="another_name")


class TestContact(TestCase):
    ''' tests contact model '''

    def setUp(self):
        self.contact = Contact.objects.create(name="contact",
                                              country="Algeria",
                                              city="Oran",
                                              function="Developer",)

    def test_create(self):
        ''' test creation '''
        self.assertEqual(self.contact.name, "contact")

    def test_update(self):
        ''' test update '''
        self.contact.name = "another_name"
        self.contact.save()
        self.assertEqual(self.contact.name, "another_name")

    def test_delete(self):
        ''' test deletion '''
        self.contact.delete()
        with self.assertRaises(Contact.DoesNotExist):
            Contact.objects.get(name="another_name")
