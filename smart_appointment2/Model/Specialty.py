from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField()

    class Meta:
        db_table = "Specialty"
