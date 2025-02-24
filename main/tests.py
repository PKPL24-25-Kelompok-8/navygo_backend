import uuid
from django.test import TestCase

from .serializers import ReservationSerializer


class ReservationTest(TestCase):
    serializer = ReservationSerializer

    def setUp(self):
        return super().setUp()

    def test_create_reservation_invalid(self):
        serializer = self.serializer(
            data={"customer_id": "1", "service_id": "1", "type": "non-blank field"}
        )
        assert not serializer.is_valid()

    def test_create_reservation_valid(self):
        customer_id = str(uuid.uuid4())
        service_id = str(uuid.uuid4())

        serializer = self.serializer(
            data={
                "customer_id": customer_id,
                "service_id": service_id,
                "type": "non-blank field",
            }
        )
        assert serializer.is_valid()

    def test_create_reservation_invalid_uuid_ver(self):
        customer_id = str(uuid.uuid1())
        service_id = str(uuid.uuid1())

        serializer = self.serializer(
            data={
                "customer_id": customer_id,
                "service_id": service_id,
                "type": "non-blank field",
            }
        )

        assert not serializer.is_valid()
