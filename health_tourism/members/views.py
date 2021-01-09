from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'Registration/create.html'
    success_url = reverse_lazy('website/templates/login')

