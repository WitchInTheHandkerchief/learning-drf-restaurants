from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurant.serializers.jsonserializers import OrdersSerializer
from restaurant.serializers.orderserializers import PlaceOrderSerializer, DishAddSerializer


@api_view(['POST'])
def place_order(request: HttpRequest) -> Response:
    serializer = PlaceOrderSerializer(data=request.data)
    if serializer.is_valid():
        created_data = serializer.create(request.data)
        response_serializer = OrdersSerializer(created_data)
        return Response(
            data=response_serializer.data, status=201
        )
    return Response(
        data=serializer.errors, status=400
    )


@api_view(['POST'])
def add_dish(request: HttpRequest) -> Response:
    serializer = DishAddSerializer(data=request.data)
    if serializer.is_valid():
        created_data = serializer.create(request.data)
        response_serializer = OrdersSerializer(created_data)
        return Response(
            data=response_serializer.data, status=201
        )
    return Response(
        data=serializer.errors, status=400
    )
