from django.urls import path
from website import views


urlpatterns = [
    path('', views.login, name="login"),
    path('home', views.home, name="home"),
    path('create', views.create, name="create"),
    path('signup', views.signup, name="signup"),
    path('feedback', views.feedback, name="feedback"),
    path('search', views.search, name="search"),
    path('Appointment', views.Appointment, name="Appointment"),
    path('documentation', views.documentation, name="documentation"),
    path('history', views.history, name="history"),
]
