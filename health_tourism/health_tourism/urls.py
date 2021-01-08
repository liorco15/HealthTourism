"""health_tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from members.views import login_view, logout_view, register_view
from website.views import contact_doctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('website/', include('website.urls')),
    path('members/login/', login_view),
    path('home/', home, name="home"),
    path('members/logout/', logout_view, name="logout"),
    path('home/create/', register_view),
    path('home/contact_doctor', contact_doctor)


]
