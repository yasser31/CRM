from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from contacts.models import Contact, Company
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

    def test_clients(self):
        ''' test get clients page'''
        response3 = self.client.get("/clients/")
        self.assertEqual(response3.status_code, 200)

    def test_details_client(self):
        ''' test get client details page '''
        client = Company.objects.create(cp_name="company",
                                        company_country="Algeria",
                                        company_city="Oran", address="address")
        url = f'/details/{client.id}'
        response4 = self.client.get(url)
        self.assertEqual(response4.status_code, 200)

    def test_thanks(self):
        ''' test get thanks page '''
        response5 = self.client.get("/thanks/")
        self.assertEqual(response5.status_code, 200)


class TestClientToProspect(TestCase):
    ''' test set and unset client '''

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="yasser", password="secret")
        self.cp = Company.objects.create(cp_name="name",
                                         company_country="Algeria",
                                         company_city="Oran",
                                         address="address",
                                         client=False)
        self.client.force_login(user)

    def test_set(self):
        ''' test set prospect to client '''
        cp = Company.objects.get(id=self.cp.id)
        response = self.client.get(f"/set/{self.cp.id}")
        data = response.json()
        self.assertTrue(data["client"])


class TestPost(TestCase):
    ''' test post requests '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="yasser", password="secret")
        self.client.force_login(self.user)

    def test_create_client(self):
        ''' test create company '''
        response = self.client.post("/add_client/",
                                    {"cp_name": "company",
                                     "address": "address",
                                     "company_country": "country",
                                     "company_city": "city",
                                     "client": 'false', })
        client = Company.objects.get(cp_name="company")
        self.assertEqual(client.cp_name, "company")
        self.assertEqual(response.resolver_match.func, views.add_client)

    def test_create_contact(self):
        cp = Company.objects.create(cp_name="name",
                                    company_country="Algeria",
                                    company_city="Oran",
                                    address="address")
        response = self.client.post(f"/add_contact/{cp.id}", {
            "name": "client",
            "country": "algeria",
            "city": "oran",
            "function": "developer",
            "email": "email@email.com",
            "user": self.user.id
        })
        contact = Contact.objects.get(name="client")
        self.assertEqual(contact.name, "client")
        self.assertEqual(response.resolver_match.func, views.add_contact)


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
        self.assertEqual(data['total_companies'], 0)
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
