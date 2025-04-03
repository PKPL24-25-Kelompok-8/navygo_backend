from django.db import models
import random

class Instansi(models.Model):
    user_id = models.UUIDField(primary_key=True)  # ID user dari service auth
    username = models.CharField(max_length=150)
    npwp = models.CharField(max_length=30, blank=True, null=True)
    nomor_rekening = models.CharField(max_length=50, blank=True, null=True)
    nama_bank = models.CharField(max_length=100, blank=True, null=True)
    jumlah_layanan_diselesaikan = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    saldo_navygo = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Jika foto_profil belum diisi, assign gambar default secara acak
        if not self.foto_profil:
            self.foto_profil = get_random_default_image()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Instansi user_id={self.user_id}"


class Pelanggan(models.Model):
    user_id = models.UUIDField(primary_key=True)  # ID user dari service auth
    username = models.CharField(max_length=150)
    saldo_navygo = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Pelanggan user_id={self.user_id}"
    
def get_random_default_image():
    # Misalnya, simpan gambar default di folder 'default_images' di dalam MEDIA_ROOT
    default_images = [
        'default_images/default1.jpg',
        'default_images/default2.jpg',
        'default_images/default3.jpg'
    ]
    return random.choice(default_images)