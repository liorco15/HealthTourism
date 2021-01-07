from django.contrib import admin
from .models import Patient
from .models import SignUp
from .models import Feedback

admin.site.register(Patient)
admin.site.register(SignUp)
admin.site.register(Feedback)
