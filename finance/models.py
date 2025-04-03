import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Bill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_created=True, editable=False)
    payment_method = models.UUIDField()

class BillStatus(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "P", _("Pending")
        CONFIRMED = "CF", _("Confirmed")
        CANCELLED = "CA", _("Cancelled")
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    def __str__(self):
        # Menggunakan get_status_display() agar menampilkan label (Pending, Confirmed, Cancelled)
        return f"{self.id} - {self.status}"

class TRBillStatus(models.Model):
    """
    Mencatat relasi antara sebuah transaksi (transaction_id) dengan BillStatus (id).
    """
    # ID utama dengan UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Relasi ke transaksi
    transaction_id = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='transaction_id')

    # Relasi ke BillStatus
    bill_status = models.ForeignKey(BillStatus, on_delete=models.CASCADE, related_name='transaction_statuses')

    # Waktu pencatatan relasi status (opsional)
    last_updated = models.DateTimeField(auto_created=True, editable=False)

    def __str__(self):
        return f"TRBillStatus: TxID={self.transaction_id} => Status={self.bill_status.status}"

class KategoriTrNavypay(models.Model):
    """
    Model untuk kategori transaksi NavyPay, misalnya:
    - top_up
    - pembayaran
    """
    KATEGORI_CHOICES = (
        ('top_up', 'Top Up'),
        ('pembayaran', 'Pembayaran'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=50, choices=KATEGORI_CHOICES, unique=True)

    def __str__(self):
        return self.nama

class TrNavypay(models.Model):
    """
    Model transaksi NavyPay untuk mencatat setiap aktivitas top-up maupun pembayaran.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Menyimpan user_id dari service auth (baik pelanggan maupun instansi)
    user_id = models.UUIDField()
    kategori = models.ForeignKey(KategoriTrNavypay, on_delete=models.CASCADE)
    nominal = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_transaksi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.kategori.nama} - {self.nominal}"