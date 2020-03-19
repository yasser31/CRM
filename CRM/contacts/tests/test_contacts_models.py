from django.test import TestCase
from ..models import Company, Departement, Contact


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


class TestClient(TestCase):
    ''' tests contact model '''
    def setUp(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)
        self.client = Contact.objects.get(name="contact")

    def test_create(self):
        ''' test creation '''
        self.assertEqual(self.client.name, "contact")

    def test_update(self):
        ''' test update '''
        self.client.name = "another_name"
        self.client.save()
        self.assertEqual(self.client.name, "another_name")

    def test_delete(self):
        ''' test deletion '''
        self.client.delete()
        with self.assertRaises(Contact.DoesNotExist):
            Contact.objects.get(name="another_name")


class TestDepartement(TestCase):
    ''' test departement model '''
    def setUp(self):
        Departement.objects.create(dep_name="IT")
        self.departement = Departement.objects.get(dep_name="IT")

    def test_create(self):
        ''' test creation '''
        self.assertEqual(self.departement.dep_name, "IT")

    def test_update(self):
        ''' test update '''
        self.departement.dep_name = "Web developement"
        self.departement.save()
        self.assertEqual(self.departement.dep_name, "Web developement")

    def test_delete(self):
        ''' test deletion '''
        self.departement.delete()
        with self.assertRaises(Departement.DoesNotExist):
            Departement.objects.get(dep_name="IT")
