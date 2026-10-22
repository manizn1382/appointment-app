from django.db import models
from .TimeModel import TimeModel


class ClinicService(TimeModel):
    clinic = models.ForeignKey("Clinic", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=4, max_digits=10)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "ClinicService"

