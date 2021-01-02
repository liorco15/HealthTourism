from django.urls import path
from website import views


urlpatterns = [
    path('', views.login, name="login"),
    path('create', views.create, name="create"),
    path('signup', views.signup, name="signup"),
    path('feedback', views.feedback, name="feedback"),
    path('search', views.search, name="search"),
]
