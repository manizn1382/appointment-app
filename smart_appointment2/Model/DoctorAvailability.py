from django.db import models
from .Doctor import Doctor


class DoctorAvailability(models.Model):

    WEEKDAYS = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="availabilities")
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    startTime = models.TimeField()
    endTime = models.TimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "DoctorAvailability"
