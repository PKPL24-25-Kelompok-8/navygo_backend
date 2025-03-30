import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BillStatus(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "P", _("Pending")
        CONFIRMED = "CF", _("Confirmed")
        CANCELLED = "CA", _("Cancelled")

    last_updated = models.DateTimeField(auto_created=True, editable=False)


class Bill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_created=True, editable=False)
    payment_method = models.UUIDField()
    status = models.ForeignKey(BillStatus, on_delete=models.CASCADE)


class Review(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    star_rating = models.DecimalField(max_digits=1, decimal_places=0)


class Reservation(models.Model):
    navygator_id = models.UUIDField()
    service_id = models.UUIDField()
    type = models.CharField(max_length=50)
    bill = models.ForeignKey(
        Bill, on_delete=models.CASCADE, related_name="reservations"
    )
