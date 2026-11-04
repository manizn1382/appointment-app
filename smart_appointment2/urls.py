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
from smart_appointment2.Views.ClinicServiceViews import ClinicServiceActions
from smart_appointment2.Views.DoctorSpecialtyViews import DocSpecialtyActions
from smart_appointment2.Views.DoctorAvailabilityViews import DocAvailabilityActions
from smart_appointment2.Views.ClinicDoctorsViews import ClinicDocActions
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('clinic', ClinicActions, basename='clinic')
router.register('user', UserActions, basename='user')
router.register('doctor', DoctorActions, basename='doctor')
router.register('specialty', SpecialtyActions, basename='specialty')
router.register('clinicService', ClinicServiceActions, basename='clinicService')
router.register('doctorSpecialty', DocSpecialtyActions, basename='doctorSpecialty')
router.register('doctorAvailability', DocAvailabilityActions, basename='doctorAvailability')
router.register('clinicDoctors', ClinicDocActions, basename='clinicDoctors')

urlpatterns = [
    path('admin/', admin.site.urls),
    *router.urls,

]
