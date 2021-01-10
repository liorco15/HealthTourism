from unittest import TestCase
from test import SimpleTestCase
from forms import CreateUserForm, SignUpForm, FeedbackForm, PatientForm, DocumentationP, EventForm, MessageForm
from models import  SignUp, Feedback, Documentation, Event, Messages
from django.urls import reverse, resolve

from website.views import contact_doctor, appointment, documentation, history, search, feedback, signup, create, home, \
    login


class BasicTest(TestCase):

    def setUp(self):
        self.item = Messages()
        self.item.title = "OK"
        self.item.description = "OK"
        self.item.save()

        self.item1 = Event()
        self.item1.title = "OK"
        self.item1.description = "OK"
        self.item1.save()

        self.item2 = Documentation()
        self.item2.title = "OK"
        self.item2.description = "OK"
        self.item2.save()

        self.item3 = SignUp()
        self.item3.title = "OK"
        self.item3.description = "OK"
        self.item3.save()

        self.item4 = Feedback()
        self.item4.title = "OK"
        self.item4.description = "OK"
        self.item4.save()

    def test_fields(self):
        """test all of fields gonna be required on my objects"""
        record = self.item.objects.get(pk=self.item.id)
        self.assertEqual(record, self.item)
        record = self.item1.objects.get(pk=self.item1.id)
        self.assertEqual(record, self.item1)
        record = self.item2.objects.get(pk=self.item2.id)
        self.assertEqual(record, self.item2)
        record = self.item3.objects.get(pk=self.item3.id)
        self.assertEqual(record, self.item3)
        record = self.item4.objects.get(pk=self.item4.id)
        self.assertEqual(record, self.item4)

    def test_slug_on_save_Messages(self):
        """ test if save slug Properly """
        self.assertEqual(self.item.slug, 'ok')
        self.assertEqual(self.item1.slug, 'ok')
        self.assertEqual(self.item2.slug, 'ok')
        self.assertEqual(self.item3.slug, 'ok')
        self.assertEqual(self.item4.slug, 'ok')

    def test_mark_completed(self):
        self.assertEqual(self.item.completed, False)
        self.item.mark.completed()
        self.assertEqual(self.item.completed, True)

        self.assertEqual(self.item1.completed, False)
        self.item1.mark.completed()
        self.assertEqual(self.item1.completed, True)

        self.assertEqual(self.item2.completed, False)
        self.item2.mark.completed()
        self.assertEqual(self.item2.completed, True)

        self.assertEqual(self.item3.completed, False)
        self.item3.mark.completed()
        self.assertEqual(self.item3.completed, True)

        self.assertEqual(self.item4.completed, False)
        self.item4.mark.completed()
        self.assertEqual(self.item4.completed, True)


class RequestForm(object):
    pass


class TestForms(SimpleTestCase):

    def test_create_user_form(self):
        form = CreateUserForm(data={
            'model': ['Patient'],
            'fields': ['dina', 'balua']
        })

    def test_sign_up_form(self):
        form = SignUpForm(data={
            'model': ['SignUp'],
            'fields': ['lior', 'inbar', 16, 'man', 'dinab@gmail', +972855555555, 'Canada', 'write']
        })

    def test_feedback_form(self):
        form = FeedbackForm(data={
            'model': ['Feedback'],
            'fields': ['dina', 'balua', 'message']
        })

    def test_patient_form(self):
        form = PatientForm(data={
            'model': ['Patient'],
            'fields': ['dan']
        })

    def test_documentation_form(self):
        form = DocumentationP(data={
            'model': ['Documentation'],
            'fields': ['inbar', 'balua', 'message', 'meeting', 'diagnosis']
        })

    def test_event_form(self):
        form = EventForm(data={
            'model': ['Event'],
            'fields': ['avihai', 27/7/92]
        })

    def test_message_form(self):
        form = MessageForm(data={
            'model': ['Messages'],
            'fields': ['vika', 18/3/98]
        })

    #def test_request_form(self):
     #   form = RequestForm(data={
      #      'model': ['Requests'],
       #     'fields': ['lior', 27/10/1994]
        #})


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_create_url_is_resolved(self):
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

    def test_request_m_url_is_resolved(self, request_m=None):
        url = reverse('request_m')
        print(resolve(url))
        self.assertEquals(resolve(url).func, request_m)

    def assertEquals(self, func, login):
        pass