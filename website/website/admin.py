from django.contrib import admin
from .models import Patient, SignUp, Feedback, Event, Messages


admin.site.register(Patient)
admin.site.register(SignUp)
admin.site.register(Feedback)
admin.site.register(Event)
admin.site.register(Messages)