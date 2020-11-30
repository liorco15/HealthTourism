from django.urls import path
from website import views



urlpatterns = [
    path('', views.contact, name="contact"),
    # path('', views.login, name="login"),
    path('join', views.join, name="join"),
    path('search', views.search, name="search"),
]
