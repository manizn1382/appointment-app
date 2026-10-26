
from django.db import models
from django.contrib.auth.models import User
from .TimeModel import TimeModel
from .TimeSlot import TimeSlot
from django.conf import settings

class Appointment(TimeModel):

    STATUS = [
        ('completed', 'COMPLETED'),
        ('cancelled', 'CANCELLED'),
        ('confirmed', 'CONFIRMED'),
        ('pending', 'PENDING'),

    ]



    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='pending', max_length=9)
    trackingCode = models.UUIDField(blank=True)
    notes = models.TextField(blank=True)
    idempotency_key = models.CharField(blank=True, max_length=255)
    cancelledAt = models.DateTimeField(blank=True)

    class Meta:
        db_table = "Appointment"
