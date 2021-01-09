from django.urls import path
from website import views
from .views import UserRegisterView


urlpatterns = [
    path('create/', UserRegisterView.as_view(), name='create'),
]
