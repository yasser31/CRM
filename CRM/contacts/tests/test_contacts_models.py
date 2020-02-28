from django.test import TestCase
from ..models import Company, Departement, Contact



class TestCompany(TestCase):
    
    def setUp(self):
        Company.objects.create(cp_name="company", company_country="Algeria",
                                company_city="Oran", address="address")
    
    def test_create(self):
        company = Company.objects.get(cp_name="company")
        self.assertEqual(company.cp_name, "company")

                        
    def test_update(self):
        company = Company.objects.get(cp_name="company")
        company.cp_name = "another_name"
        company.save()
        self.assertEqual(company.cp_name, "another_name")

class TestClient(TestCase):
    
    def setUp(self):
        Contact.objects.create(name="contact", country="Algeria",
                                city="Oran", function="Developer",
                                client=False)
    
    def test_create(self):
        client = Contact.objects.get(name="contact")
        self.assertEqual(client.name, "contact")

                        
    def test_update(self):
        client = Contact.objects.get(name="contact")
        client.name = "another_name"
        client.save()
        self.assertEqual(client.name, "another_name")