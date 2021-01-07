from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.urls import reverse_lazy


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'register/register.html'
#     success_url = reverse_lazy('login')
# Create your views here.

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


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('b/')
    context = {
        'form': form,
    }
    return render(request, "create.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
