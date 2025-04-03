from django.db import models

from finance.models import *


# Create your models here.
class Reservation(models.Model):
    navygator_id = models.UUIDField()
    service_id = models.UUIDField()
    type = models.CharField(max_length=50)
    bill = models.ForeignKey(
        Bill, on_delete=models.CASCADE, related_name="reservations"
    )
