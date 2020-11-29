from django.urls import path
from website import views

urlpatterns = [
    path('', views.login, name="login"),
    path('join', views.join, name="join"),
]