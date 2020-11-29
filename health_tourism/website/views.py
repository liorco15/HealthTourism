from django.shortcuts import render
from .models import Patient
from .forms import PatientForm


def login(request):
    all_patients = Patient.objects.all
    return render(request, 'login.html', {'all':all_patients})


def join(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'login.html', {})
    else:
        return render(request, 'join.html', {})