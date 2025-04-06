# serializers.py
from rest_framework import serializers
from .models import City, Ocean, Port

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
