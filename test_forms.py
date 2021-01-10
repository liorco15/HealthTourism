from django.test import SimpleTestCase
from website.forms import CreateUserForm, SignUpForm, FeedbackForm, PatientForm, DocumentationP, EventForm, MessageForm, RequestForm
from website.models import Patient, SignUp, Feedback, Documentation, Event, Messages, Requests

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

    def test_request_form(self):
        form = RequestForm(data={
            'model': ['Requests'],
            'fields': ['lior', 27/10/1994]
        })
