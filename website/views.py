from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from health_tourism.functions import full_name_fix, name_fix
from .forms import CreateUserForm, SignUpForm, FeedbackForm, Patient


def login(request):
    return render(request, 'login.html', {})


def create(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'create.html', {})
    else:
        return render(request, 'create.html', {})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'signup.html', {})
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
            user_search = Patient.objects.filter(Q(first_name=full_name_fix(patient)[0]) & Q(last_name=full_name_fix(patient)[1]))
            return render(request, 'search.html', {'patients': user_search})
        except IndexError:
            pass
        try:
            # search by first name
            patient = request.POST.get('search')
            user_search = Patient.objects.filter(first_name=name_fix(patient))
            if len(user_search) > 0:
                return render(request, 'search.html', {'patients': user_search})
        except IndexError:
            pass
        try:
            # search by last name
            patient = request.POST.get('search')
            user_search = Patient.objects.filter(last_name=name_fix(patient))
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