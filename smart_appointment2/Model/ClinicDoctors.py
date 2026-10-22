from django.db import models


class ClinicDoctors(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    clinic = models.ForeignKey("Clinic", on_delete=models.CASCADE)

    class Meta:
        db_table = "ClinicDoctors"
