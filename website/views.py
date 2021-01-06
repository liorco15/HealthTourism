from django.shortcuts import render
from.models import Event
from.forms import EventForm


def home(request):
    all_events = Event.objects.all
    return render(request, 'home.html', {'all': all_events})

def Appointment(request):
    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'Appointment.html',{})
    else:
        return render(request,'Appointment.html', {})

def documentation(request):
    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'documentation.html',{})
    else:
        return render(request,'documentation.html', {})