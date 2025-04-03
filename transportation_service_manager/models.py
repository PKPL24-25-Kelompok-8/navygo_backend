## Standard library imports
from django.db import models
import uuid

## Third-party library imports
pass

## Local project imports
pass

class Vehicle(models.model):
    id = models.BigIntegerField(primary_key=true)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    vehicle_name = models.CharField(max_length=255)
    vehichle_type = models.CharField(max_length=255)
    capacity = models.IntegerField()

    # Validator
    def save(self, *args, **kwargs):
        if self.vehicle_name.empty():
            raise ValueError("Vehicle name cannot be empty.")
        
        if self.vehicle_name.length() > 255:
            raise ValueError("Vehicle name cannot exceed 255 characters.")
        
        if self.vehichle_type.empty(): 
            raise ValueError("Vehicle type cannot be empty")
        
        if self.vehichle_type.length() > 255:
            raise ValueError("Vehicle type cannot exceed 255 characters.")
        
        if self.capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")

        super().save(*args, **kwargs)

    # Return All Fields
    def __str__(self):
        return ", ".join(f"{field.name}: {getattr(self, field.name)}" 
                         for field in self._meta.fields)

class Harbour(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    harbour_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ocean = models.ForeignKey('Ocean', on_delete=models.CASCADE, related_name='harbours')
    kota = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.harbour_name.strip() == "":
            raise ValueError("Harbour name cannot be empty.")
        
        if len(self.harbour_name) > 255:
            raise ValueError("Harbour name cannot exceed 255 characters.")
        
        if self.location.strip() == "":
            raise ValueError("Location cannot be empty.")
        
        if len(self.location) > 255:
            raise ValueError("Location cannot exceed 255 characters.")

        super().save(*args, **kwargs)

    def __str__(self):
        return ", ".join(f"{field.name}: {getattr(self, field.name)}" for field in self._meta.fields)
    
class Ocean(models.model):
    id = models.IntegerField(primary_key=true)
    ocean_name = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if self.ocean_name.empty():
            raise ValueError("Ocean name cannot be empty.")
        
        if self.ocean_name.length() > 255:
            raise ValueError("Ocean name cannot exceed 255 characters.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return ", ".join(f"{field.name}: {getattr(self, field.name)}" for field in self._meta.fields)
    
