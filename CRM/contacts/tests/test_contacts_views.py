from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from contacts.models import Contact, Company, Departement
from contacts import views


class TestGet(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)

    def test_get_contacts(self):
        response1 = self.client.get("/contacts/")
        self.assertEqual(response1.status_code, 200)

    def test_prospects(self):
        response2 = self.client.get("/prospects/")
        self.assertEqual(response2.status_code, 200)

    def test_clients(self):
        response3 = self.client.get("/clients/")
        self.assertEqual(response3.status_code, 200)

    def test_details(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)
        contact = Contact.objects.get(name="contact")
        url = f'/details/{contact.id}'
        response4 = self.client.get(url)
        self.assertEqual(response4.status_code, 200)

    def test_thanks(self):
        response5 = self.client.get("/thanks/")
        self.assertEqual(response5.status_code, 200)


class TestClientToProspect(TestCase):

    def setUp(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)

    def test_set(self):
        contact = Contact.objects.get(name="contact")
        contact.client = True
        contact.save()
        self.assertTrue(contact.client)

    def test_unset(self):
        contact = Contact.objects.get(name="contact")
        contact.client = False
        contact.save()
        self.assertFalse(contact.client)


class TestPost(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)

    def test_create_company(self):
        response = self.client.post("/add_company/",
                                    {"cp_name": "company",
                                     "address": "address",
                                     "company_country": "country",
                                     "company_city": "city"})
        company = Company.objects.get(cp_name="company")
        self.assertEqual(company.cp_name, "company")
        self.assertEqual(response.resolver_match.func, views.add_company)
        response2 = self.client.post("/add_departement/",
                                     {"dep_name": "IT"})

        dep = Departement.objects.get(dep_name="IT")
        self.assertEqual(dep.dep_name, "IT")
        self.assertEqual(response2.resolver_match.func,
                         views.add_departement)
        response3 = self.client.post("/add_contact/", {
            "name": "client",
            "country": "algeria",
            "city": "oran",
            "function": "developer",
            "client": False
        })
        contact = Contact.objects.get(name="client")
        self.assertEqual(contact.name, "client")
        self.assertEqual(response3.resolver_match.func, views.add_contact)


class TestStat(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)

    def test_cl_pros_percent(self):
        response = self.client.get("/contact_percent/")
        data = response.json()
        self.assertEqual(data['total_contacts'], 0)
        self.assertEqual(data["total_clients"], 0)
        self.assertEqual(data["total_prospects"], 0)
        self.assertEqual(data["clients_percent"], 0)
        self.assertEqual(data["prospects_percent"], 0)

    def test_contact_month(self):
        response = self.client.get("/contact_month/")
        data = response.json()
        self.assertTrue(data)
        self.assertTrue(data)

    def test_recent_contact(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=True)
        response = self.client.get("/recent_contact/")
        data = response.json()
        self.assertEqual(data["contact"], [])
        self.assertEqual(data["client"][0]["city"], "Oran")
