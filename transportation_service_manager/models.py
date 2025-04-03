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

