from django import forms
from .models import Patient
from .models import Contact


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'age', 'gender', 'email', 'phone_number', 'country', 'reason_for_referral']
