from .forms import SignUpForm, FeedbackForm
from .models import Patient
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from members.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.urls import reverse_lazy


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'register.html', {})
    else:
        return render(request, 'register.html', {})


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {})
        return render(request, 'feedback.html', {})
    else:
        return render(request, 'feedback.html', {})


def profil(request):
    my_profil = Patient.objects.all
    return render(request, 'profil.html', {'all': my_profil})

