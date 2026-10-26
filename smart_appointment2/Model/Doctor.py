
from django.contrib.auth.models import User
from django.db import models

from .DoctorSpecialty import DoctorSpecialty
from .Specialty import Specialty
from .Clinic import Clinic
from .ClinicDoctors import ClinicDoctors
from .TimeModel import TimeModel
from django.conf import settings


class Doctor(TimeModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    medicalLicense = models.CharField(max_length=255, unique=True)
    specialties = models.ManyToManyField(Specialty, through=DoctorSpecialty, related_name="doctors")
    clinics = models.ManyToManyField(Clinic, through=ClinicDoctors, related_name="doctors")

    class Meta:
        db_table = "Doctor"
