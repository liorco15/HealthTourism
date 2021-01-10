from django.urls import path
from website import views


urlpatterns = [
    path('', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('create', views.create, name="create"),
    path('create/update_patient', views.create, name="update_patient"),
    path('signup', views.signup, name="signup"),
    path('feedback', views.feedback, name="feedback"),
    path('search', views.search, name="search"),
    path('appointment', views.appointment, name="appointment"),
    path('documentation', views.documentation, name="documentation"),
    path('history', views.history, name="history"),
    path('contact_doctor', views.contact_doctor, name="contact_doctor"),
    path('request_m', views.request_m, name="request_m"),
]
