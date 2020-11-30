from django.contrib import admin
from .models import Patient
from .models import Contact

admin.site.register(Patient)
admin.site.register(Contact)
