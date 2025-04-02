import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
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
