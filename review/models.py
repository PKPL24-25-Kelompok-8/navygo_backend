from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from finance.models import Bill

# Create your models here.
class Review(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    star_rating = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
