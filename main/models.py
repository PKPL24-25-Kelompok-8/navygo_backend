import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Reservation(models.Model):
    customer_id = models.UUIDField()
    service_id = models.UUIDField()
    type = models.CharField(max_length=50)


class BillStatus(models.Model):
    class StatusChoices(models.TextChoices):
        CONFIRMED = "CF", _("Confirmed")
        CANCELLED = "CA", _("Cancelled")

    last_updated = models.DateTimeField(auto_created=True, editable=False)


class Bill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_created=True, editable=False)
    reservations = models.ManyToManyField(Reservation, related_name="transaction")
    payment_method = models.UUIDField()
