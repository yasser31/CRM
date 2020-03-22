from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from contacts.models import Contact, Company, Departement
from contacts import views


class TestGet(TestCase):
    ''' tests get requests'''

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.client.force_login(user)

    def test_get_contacts(self):
        ''' test get contact page'''
        response1 = self.client.get("/contacts/")
        self.assertEqual(response1.status_code, 200)

    def test_prospects(self):
        ''' test get prospects page '''
        response2 = self.client.get("/prospects/")
        self.assertEqual(response2.status_code, 200)

    def test_clients(self):
        ''' test get clients page'''
        response3 = self.client.get("/clients/")
        self.assertEqual(response3.status_code, 200)

    def test_details(self):
        ''' test get client details page '''
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)
        contact = Contact.objects.get(name="contact")
        url = f'/details/{contact.id}'
        response4 = self.client.get(url)
        self.assertEqual(response4.status_code, 200)

    def test_thanks(self):
        ''' test get thanks page '''
        response5 = self.client.get("/thanks/")
        self.assertEqual(response5.status_code, 200)


class TestClientToProspect(TestCase):
    ''' test set and unset client '''

    def setUp(self):
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=False)

    def test_set(self):
        ''' test set prospect to client '''
        contact = Contact.objects.get(name="contact")
        contact.client = True
        contact.save()
        self.assertTrue(contact.client)

    def test_unset(self):
        ''' test set client to prospect '''
        contact = Contact.objects.get(name="contact")
        contact.client = False
        contact.save()
        self.assertFalse(contact.client)


class TestPost(TestCase):
    ''' test post requests '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="yasser", password="secret")
        self.client.force_login(self.user)

    def test_create_contact(self):
        ''' test create company departement contact '''
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
            "client": False,
            "user": self.user.id
        })
        contact = Contact.objects.get(name="client")
        self.assertEqual(contact.name, "client")
        self.assertEqual(response3.resolver_match.func, views.add_contact)


class TestStat(TestCase):
    ''' test statitstics '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="yasser", password="secret")
        self.client.force_login(self.user)

    def test_cl_pros_percent(self):
        ''' test client prospects percent '''
        response = self.client.get("/contact_percent/")
        data = response.json()
        self.assertEqual(data['total_contacts'], 0)
        self.assertEqual(data["total_clients"], 0)
        self.assertEqual(data["total_prospects"], 0)
        self.assertEqual(data["clients_percent"], 0)
        self.assertEqual(data["prospects_percent"], 0)

    def test_contact_month(self):
        ''' test contacts per month '''
        response = self.client.get("/contact_month/")
        data = response.json()
        self.assertTrue(data)
        self.assertTrue(data)

    def test_recent_contact(self):
        ''' test recent contact '''
        Contact.objects.create(name="contact", country="Algeria",
                               city="Oran", function="Developer",
                               client=True, user=self.user)
        response = self.client.get("/recent_contact/")
        data = response.json()
        self.assertEqual(data["contact"][0]["name"], "contact")
