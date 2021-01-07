from django import forms
from .models import Patient, SignUp, Feedback, Event


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name', 'last_name', 'age', 'gender', 'email', 'phone_number', 'country', 'reason_for_referral']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'message']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','date']