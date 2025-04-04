from django.db import models

from finance.models import *
from transportation_service_manager.models import *
from user_management.models import *


# Create your models here.
class Reservation(models.Model):
    '''
    id by [KODE KAPAL][JENIS KAPAL][INISIAL USER][BERAPA PASSENGER]
    [TANGGAL DEPARTURE][JAM KEBERANGKATAN][ESTIMATEDDURATION (MIN)]
    [DAH COBA BERAPA KALI TRANSAKSI YANG SAMA][CHECKSUM]
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    navygator_id = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name="reservation")
    service_id = models.ForeignKey(TransportationService, on_delete=models.CASCADE, related_name="reservation")
    type = models.CharField(max_length=50)
    bill = models.ForeignKey(
        Bill, on_delete=models.CASCADE, related_name="reservation"
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
