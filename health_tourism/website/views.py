from django.shortcuts import render
from .models import Patient
from .forms import PatientForm
from .models import Contact
from .forms import ContactForm


def login(request):
    all_patients = Patient.objects.all
    return render(request, 'login.html', {'all':all_patients})


def join(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})
    else:
        return render(request, 'join.html', {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})
    else:
        return render(request, 'contact.html', {})


def search(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})
    else:
        return render(request, 'search.html', {})