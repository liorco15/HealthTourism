from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import login, create, signup, feedback, search, home, history, documentation, appointment, contact_doctor, request_m


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_list_url_is_resolved(self):
        url = reverse('create')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)

    def test_feedback_url_is_resolved(self):
        url = reverse('feedback')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feedback)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_history_url_is_resolved(self):
        url = reverse('history')
        print(resolve(url))
        self.assertEquals(resolve(url).func, history)

    def test_documentation_url_is_resolved(self):
        url = reverse('documentation')
        print(resolve(url))
        self.assertEquals(resolve(url).func, documentation)

    def test_appointment_url_is_resolved(self):
        url = reverse('appointment')
        print(resolve(url))
        self.assertEquals(resolve(url).func, appointment)

    def test_contact_doctor_url_is_resolved(self):
        url = reverse('contact_doctor')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact_doctor)

    def test_request_m_url_is_resolved(self):
        url = reverse('request_m')
        print(resolve(url))
        self.assertEquals(resolve(url).func, request_m)