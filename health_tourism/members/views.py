from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'Registration/create.html'
#     success_url = reverse_lazy('login')


def create2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'create.html', {'form': form})



