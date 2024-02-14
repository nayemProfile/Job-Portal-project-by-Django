"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singupPage/',singupPage,name="singupPage"),
    path('loginPage/',loginPage,name="loginPage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('viewjobPage/',viewjobPage,name="viewjobPage"),
    path('jobAdd/',jobAdd,name="jobAdd"),
    path('editjob/',editjob,name="editjob"),
    path('deletejob/',deletejob,name="deletejob"),
    path('search/',search,name="search"),
    
    
]
