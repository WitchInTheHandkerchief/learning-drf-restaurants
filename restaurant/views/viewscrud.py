from rest_framework.viewsets import ModelViewSet

from restaurant.models import Dishes, Portions, Waiters, Rooms, Tables, Orders, Addresses, User, Reservations, Couriers, \
    Delivery
from restaurant.serializers import jsonserializers


class DishesCRUD(ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = jsonserializers.DishesSerializer


class PortionsCRUD(ModelViewSet):
    queryset = Portions.objects.all()
    serializer_class = jsonserializers.PortionsSerializer


class WaitersCRUD(ModelViewSet):
    queryset = Waiters.objects.all()
    serializer_class = jsonserializers.WaitersSerializer


class RoomsCRUD(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = jsonserializers.RoomsSerializer


class TablesCRUD(ModelViewSet):
    queryset = Tables.objects.all()
    serializer_class = jsonserializers.TablesSerializer


class OrdersCRUD(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = jsonserializers.OrdersSerializer


class AddressesCRUD(ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = jsonserializers.AddressesSerializer


class UserCRUD(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = jsonserializers.UserSerializer


class ReservationsCRUD(ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = jsonserializers.ReservationsSerializer


class CouriersCRUD(ModelViewSet):
    queryset = Couriers.objects.all()
    serializer_class = jsonserializers.CouriersSerializer


class DeliveryCRUD(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = jsonserializers.DeliverySerializer
