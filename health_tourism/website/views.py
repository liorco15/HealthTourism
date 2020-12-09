from django.shortcuts import render
from .forms import CreateUserForm
from .forms import SignUpForm
from .forms import FeedbackForm


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
