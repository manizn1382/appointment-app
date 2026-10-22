from django.db import models
from .TimeModel import TimeModel
from .Doctor import Doctor
from .ClinicService import ClinicService


class TimeSlot(TimeModel):

    STATUS = [
        ('r', 'RESERVED'),
        ('b', 'BOOKED'),
        ('a', 'AVAILABLE'),

    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="timeslots")
    clinicService = models.ForeignKey(ClinicService, on_delete=models.CASCADE)
    startAt = models.DateTimeField()
    endAt = models.DateTimeField()
    status = models.CharField(choices=STATUS, default='a', max_length=2)

    class Meta:
        db_table = "TimeSlot"

