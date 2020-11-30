from django import forms
from .models import Patient
from .models import SignUp
from .models import Feedback


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