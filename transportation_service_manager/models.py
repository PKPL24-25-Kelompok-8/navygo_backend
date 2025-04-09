## Standard library imports
from django.db import models
import uuid

## Third-party library imports
pass

## Local project imports
pass

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Ocean(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Port(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ocean = models.ForeignKey(Ocean, on_delete=models.CASCADE, related_name="ports_ocean")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="ports_city")

class Vehicle(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('Cruise Ship', 'Cruise Ship'),
        ('Ocean Liner', 'Ocean Liner'),
        ('Ferry', 'Ferry'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    capacity = models.IntegerField()

class PortVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    current_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="portvisit_vehicle")
    current_port = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="portvisit_current")
    port_destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="portvisit_desitnation")
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

class TransportationService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    port_visit = models.ForeignKey(PortVisit, on_delete=models.CASCADE, related_name="transportation_service_port_visit")
    status = models.ForeignKey('StatusTransportationService', on_delete=models.CASCADE, related_name="transportation_service_status")
    price = models.DecimalField(max_digits=10, decimal_places=2)

class StatusTransportationService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('Pending', 'Waiting For Payment'),
        ('Paid', 'Payment Confirmed'),
        ('Ticket Issued', 'Ticket Issued'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('Refunded', 'Refunded'),
        ('Checked In', 'Checked In'),
        ('Boarded', 'On Board'),
        ('Delayed', 'Delayed'),
        ('Completed', 'Completed'),
        ('Expired', 'Expired'),
        ('No Show', 'No Show'),
        ('Refund Requested', 'Refund Requested'),
        ('Refund Approved', 'Refund Approved'),
        ('Refund Denied', 'Refund Denied'),
        ('Refund Processed', 'Refund Processed'),
        ('Refund Completed', 'Refund Completed'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)