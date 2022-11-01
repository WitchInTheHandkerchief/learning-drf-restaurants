from typing import Any

from rest_framework import serializers

from restaurant import models


class PlaceOrderSerializer(serializers.Serializer):
    def create(self, validated_data: dict[str: Any]):
        delivery = validated_data.get("with_delivery")
        data = models.Orders.objects.create(
            with_delivery=delivery
        )
        return data

    def validate(self, attrs):
        return attrs
