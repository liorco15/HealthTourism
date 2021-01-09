from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from health_tourism.functions import full_name_fix, name_fix
from .forms import CreateUserForm, SignUpForm, FeedbackForm, Patient, EventForm, DocumentationP, MessageForm
from .models import Event, Messages, Documentation, Profile


def login(request):
    return render(request, 'login.html', {})


def create(request):
    # if request.method == "POST":
    #     form = CreateUserForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     return render(request, 'create.html', {})
    # else:
    #     return render(request, 'create.html', {})

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form2 = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # form2.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return render(request, 'home.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'create.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, "Your request has been successfully submitted!")
        return render(request, 'login.html', {})
    else:
        return render(request, 'signup.html', {})


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {})
        return render(request, 'feedback.html', {})
    else:
        return render(request, 'feedback.html', {})


def search(request):
    """
    search patient panel
    :param request: user  input
    :return: result of patients
    """
    if request.method == "POST":
        try:
            # search both first and last name
            patient = request.POST.get('search')
            user_search = Profile.objects.filter(
                Q(first_name=full_name_fix(patient)[0]) & Q(last_name=full_name_fix(patient)[1]))
            return render(request, 'search.html', {'patients': user_search})
        except IndexError:
            pass
        try:
            # search by first name
            patient = request.POST.get('search')
            user_search = Profile.objects.filter(first_name=name_fix(patient))
            if len(user_search) > 0:
                return render(request, 'search.html', {'patients': user_search})
        except IndexError:
            pass
        try:
            # search by last name
            patient = request.POST.get('search')
            user_search = Profile.objects.filter(last_name=name_fix(patient))
            if len(user_search) > 0:
                return render(request, 'search.html', {'patients': user_search})
            else:
                msg = "The user does not exist."
                return render(request, 'search.html', {'patients': msg})
        except IndexError:
            msg = "The user does not exist."
            return render(request, 'search.html', {'patients': msg})
    else:
        return render(request, 'search.html', {})


def home(request):
    all_messages = Messages.objects.all
    all_events = Event.objects.all
    return render(request, 'home.html', {'events': all_events, 'messages': all_messages})


def history(request):
    # user_history = Documentation.objects.all
    # user_history = Profile.objects.all().select_related('profile')
    patient = request.POST['user_name']
    # if 'Donald' in request.GET:
    #     user_history = Profile.objects.get(first_name="Donald")
    user_search = Profile.objects.filter(
        Q(first_name=full_name_fix(patient)[0]) & Q(last_name=full_name_fix(patient)[1]))
    return render(request, 'history.html', {'history': user_search})
    # return render(request, 'search.html', {})


def documentation(request):
    if request.method == "POST":
        form = DocumentationP(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
        return render(request, 'documentation.html', {})
    else:
        return render(request, 'documentation.html', {})


def appointment(request):
    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'appointment.html', {})
    else:
        return render(request, 'appointment.html', {})


def contact_doctor(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
        return render(request, 'contact_doctor.html', {})
    else:
        return render(request, 'contact_doctor.html', {})


