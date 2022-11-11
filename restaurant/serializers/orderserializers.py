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


class DishAddSerializer(serializers.Serializer):
    def validate(self, attrs):
        order_id = attrs.get('order_id')
        dish_id = attrs.get('dish_id')
        if not models.Orders.objects.filter(id=order_id).exists:
            raise serializers.ValidationError(
                'Order does not exist'
            )
        if not models.Dishes.objects.filter(id=dish_id).exists:
            raise serializers.ValidationError(
                'Dish does not exist'
            )
        return attrs

    def create(self, validated_data):
        order_id = validated_data.get('order_id')
        dish_id = validated_data.get('dish_id')
        order = models.Orders.objects.filter(id=order_id).last()
        dish = models.Dishes.objects.filter(id=dish_id).last()
        order.dishes.add(dish)
        return_data = order.save()
        return return_data
