## Standard library imports
from django.db import models
import uuid

## Third-party library imports
pass

## Local project imports
pass

class City(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Ocean(models.Model):
    name = models.CharField(max_length=255)

class Port(models.Model):
    name = models.CharField(max_length=255)
    ocean = models.ForeignKey(Ocean, on_delete=models.CASCADE, related_name="ports")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="ports")

class Vehicle(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    current_port = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehicles")

class PortVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    current_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="portvisit")
    current_port = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="portvisit")
    port_destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="portvisit")
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

class TransportationService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    port_visit = models.ForeignKey(PortVisit, on_delete=models.CASCADE, related_name="transportation_service")
    status = models.ForeignKey('StatusTransportationService', on_delete=models.CASCADE, related_name="transportation_service")
    price = models.DecimalField(max_digits=10, decimal_places=2)

class StatusTransportationService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)