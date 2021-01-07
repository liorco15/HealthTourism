from django.urls import path
from website import views


urlpatterns = [

    path('signup', views.signup, name="signup"),
    path('feedback', views.feedback, name="feedback"),
    path('home/profil', views.profil, name="profil"),

]
