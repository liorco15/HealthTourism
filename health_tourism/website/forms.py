from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Patient
from .models import SignUp
from .models import Feedback


# class CreateUserForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['first_name', 'last_name']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name', 'last_name', 'age', 'gender', 'email', 'phone_number', 'country', 'reason_for_referral']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'message']

#
# User = get_user_model()

#
# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError('user not found')
#             if not user.check_password(password):
#                 raise forms.ValidationError('Wrong Password, please try again')
#
#             return super(UserLoginForm, self).clean(*args, **kwargs)
#
#
# class UserRegisterForm(forms.ModelForm):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
