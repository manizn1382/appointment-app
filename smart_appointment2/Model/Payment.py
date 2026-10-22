from django.db import models
from .Appointment import Appointment
from .TimeModel import TimeModel


class Payment(TimeModel):

    STATUS = [
        ('paid', 'PAID'),
        ('pend', 'PENDING'),
        ('cancelled', 'CANCELLED'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=4, max_digits=10)
    status = models.CharField(choices=STATUS, max_length=10)
    transaction_id = models.CharField(max_length=255)
    paidAt = models.DateTimeField(blank=True)

    class Meta:
        db_table = "Payment"
