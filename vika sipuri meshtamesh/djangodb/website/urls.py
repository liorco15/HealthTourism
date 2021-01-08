from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Appointment', views.Appointment, name="Appointment"),
    path('documentation', views.documentation, name="documentation"),
]