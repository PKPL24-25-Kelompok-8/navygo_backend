from rest_framework import serializers
from .models import Reservation

import re


class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["navygator_id", "service_id", "type"]

    def validate(self, data):

        if not self.is_valid_uuid(str(data["navygator_id"])):
            raise serializers.ValidationError(
                {"navygator_id": "Customer ID doesn't conform to UUID v4 standards."}
            )

        if not self.is_valid_uuid(str(data["service_id"])):
            raise serializers.ValidationError(
                {"service_id": "Service ID doesn't conform to UUID v4 standards."}
            )

        return data

    @classmethod
    def is_valid_uuid(cls, uuid: str) -> bool:
        uuid_regex = re.compile(
            r"^[a-fA-F0-9]{8}\-[a-fA-F0-9]{4}\-4[a-fA-F0-9]{3}\-[89abAB][a-fA-F0-9]{3}\-[a-fA-F0-9]{12}$"
        )

        return bool(uuid_regex.match(uuid))


class EditReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["type"]
