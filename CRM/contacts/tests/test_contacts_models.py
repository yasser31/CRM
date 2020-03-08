from django.test import TestCase
from ..models import Company, Departement, Contact


class TestCompany(TestCase):

    def setUp(self):
        Company.objects.create(cp_name="company", company_country="Algeria",
                               company_city="Oran", address="address")
        self.company = Company.objects.get(cp_name="company")

    def test_create(self):
        self.assertEqual(self.company.cp_name, "company")

    def test_update(self):
        self.company.cp_name = "another_name"
        self.company.save()
        self.assertEqual(self.company.cp_name, "another_name")

    def test_delete(self):
        self.company.delete()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(cp_name="another_name")


class TestClient(TestCase):
    def setUp(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)
        self.client = Contact.objects.get(name="contact")

    def test_create(self):
        self.assertEqual(self.client.name, "contact")

    def test_update(self):
        self.client.name = "another_name"
        self.client.save()
        self.assertEqual(self.client.name, "another_name")

    def test_delete(self):
        self.client.delete()
        with self.assertRaises(Contact.DoesNotExist):
            Contact.objects.get(name="another_name")


class TestDepartement(TestCase):
    def setUp(self):
        Departement.objects.create(dep_name="IT")
        self.departement = Departement.objects.get(dep_name="IT")

    def test_create(self):
        self.assertEqual(self.departement.dep_name, "IT")

    def test_update(self):
        self.departement.dep_name = "Web developement"
        self.departement.save()
        self.assertEqual(self.departement.dep_name, "Web developement")

    def test_delete(self):
        self.departement.delete()
        with self.assertRaises(Departement.DoesNotExist):
            Departement.objects.get(dep_name="IT")
