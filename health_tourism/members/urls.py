from django.urls import path
from .views import register_view
from members.views import login_view

urlpatterns = [
    path('create/', register_view, name='create'),
    path('members/login', login_view),
]
