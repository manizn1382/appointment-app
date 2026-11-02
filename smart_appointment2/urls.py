"""
URL configuration for smart_appointment2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from smart_appointment2.Views.ClinicViews import ClinicActions
from smart_appointment2.Views.UserViews import UserActions
from smart_appointment2.Views.DoctorViews import DoctorActions
from smart_appointment2.Views.SpecialtyViews import SpecialtyActions

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('clinic', ClinicActions, basename='clinic')
router.register('user', UserActions, basename='user')
router.register('doctor', DoctorActions, basename='doctor')
router.register('specialty', SpecialtyActions, basename='specialty')

urlpatterns = [
    path('admin/', admin.site.urls),
    *router.urls,

]
