from rest_framework import mixins, viewsets
from .models import Reservation
from .serializers import CreateReservationSerializer, EditReservationSerializer
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CreateReservationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CreateReservationSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(navygator_id=self.request.user.user_id)


class EditReservationViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = EditReservationSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(navygator_id=self.request.user.user_id)
