from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Patient, SignUp, Feedback, Event, Documentation, Messages, Profile


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'email', 'phone_number', 'country']


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


class DocumentationP(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ['first_name', 'last_name','reason_why','meeting','diagnosis']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','date']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['subject', 'new_message']


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('user not found')
            if not user.check_password(password):
                raise forms.ValidationError('Wrong Password, please try again')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data('email')
        email2 = self.cleaned_data('email2')
        if email != email2:
            raise forms.ValidationError("emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
