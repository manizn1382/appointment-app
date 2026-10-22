from django.db import models


class DoctorSpecialty(models.Model):

    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    specialty = models.ForeignKey("Specialty", on_delete=models.CASCADE)

    class Meta:
        db_table = "DoctorSpecialty"
