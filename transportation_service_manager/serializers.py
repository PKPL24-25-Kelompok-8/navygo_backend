# serializers.py
from rest_framework import serializers
from .models import City, Ocean, Port, Vehicle, PortVisit

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class OceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocean
        fields = '__all__'

class PortSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    ocean = OceanSerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city', write_only=True)
    ocean_id = serializers.PrimaryKeyRelatedField(
        queryset=Ocean.objects.all(), source='ocean', write_only=True)

    class Meta:
        model = Port
        fields = ['id', 'name', 'ocean', 'ocean_id', 'city', 'city_id']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class PortVisitSerializer(serializers.ModelSerializer):
    current_vehicle = VehicleSerializer(read_only=True)
    current_port = PortSerializer(read_only=True)
    port_destination = PortSerializer(read_only=True)
    current_vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='current_vehicle', write_only=True)
    current_port_id = serializers.PrimaryKeyRelatedField(
        queryset=Port.objects.all(), source='current_port', write_only=True)
    port_destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Port.objects.all(), source='port_destination', write_only=True)

    class Meta:
        model = PortVisit
        fields = ['id', 'current_vehicle', 'current_vehicle_id', 'current_port', 'current_port_id', 'port_destination', 'port_destination_id', 'arrival_time', 'departure_time']

