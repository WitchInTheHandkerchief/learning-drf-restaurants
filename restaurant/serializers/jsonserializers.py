from rest_framework import serializers
from restaurant import models


class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dishes
        fields = "__all__"


class PortionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portions
        fields = "__all__"


class WaitersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Waiters
        fields = "__all__"


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rooms
        fields = "__all__"


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tables
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = "__all__"


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Addresses
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservations
        fields = "__all__"


class CouriersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Couriers
        fields = "__all__"


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        fields = "__all__"

