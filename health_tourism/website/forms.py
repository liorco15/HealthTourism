from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']
            # , 'age', 'gender', 'email', 'phone_number', 'country', 'reason_for_referral']