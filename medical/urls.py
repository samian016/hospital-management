"""Hospital_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import login.views as login_view
import medical.views as medical_views


urlpatterns = [
    path('m/', medical_views.medical),
    path('add/', medical_views.add, name="addP"),
    path('patient/id=<int:id>', medical_views.profile, name="profile"),
    path('patients/', medical_views.list, name="list"),
    path('update/id=<int:id>', medical_views.update),
    path('delete/id=<int:id>', medical_views.delete),
    path('release/id=<int:id>', medical_views.release),
    path('case-summary/id=<int:id>', medical_views.summary),
    path('death/id=<int:id>', medical_views.death),

]