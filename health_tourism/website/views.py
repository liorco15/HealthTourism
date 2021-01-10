from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from health_tourism.functions import full_name_fix, name_fix
from .forms import SignUpForm, FeedbackForm, EventForm, MessageForm, UserLoginForm, RequestForm
from .models import Event, Messages, Profile


def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            flag = 0
            update_patient(request, user, flag)
            return render(request, 'home.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'create.html', {'form': form})


def update_patient(request, user2, flag):
    if flag == 1:
        if request.method == 'POST':
            patient = request.POST['user_name']
            user = Profile.objects.get(username=patient)
            f_name = request.POST['first_name']
            l_name = request.POST['last_name']
            passport = request.POST['passport']
            user.first_name = f_name
            user.last_name = l_name
            user.passport = passport
            user.save()
            return
    else:
        flag = 1
        return render(request, 'update_patient.html', {'patient': user2})


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
    if request.method == "POST":
        patient = request.POST['passport_number']
        user = Profile.objects.filter(passport=patient)
        return render(request, 'history.html', {'history': user})
    else:
        return render(request, 'search.html', {})


def documentation(request):
    if request.method == "POST":
        patient = request.POST['patients']
        reason_why = request.POST['reason_why']
        meeting = request.POST['meeting']
        user = Profile.objects.get(passport=patient)
        user.reason_why = reason_why
        user.meeting = meeting
        user.save()
        return render(request, 'home.html', {})
    else:
        profiles = Profile.objects.all()
        return render(request, 'documentation.html', {'patients': profiles})


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


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home/')
    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect('login.html')


def request_m(request):
    if request.method == "POST":
        form = RequestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
        return render(request, 'request_m.html', {})
    else:
        return render(request, 'request_m.html', {})