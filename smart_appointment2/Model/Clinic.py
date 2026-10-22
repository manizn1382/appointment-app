from django.db import models
from .TimeModel import TimeModel


class Clinic(TimeModel):

    name = models.CharField(max_length=255)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Clinic"
