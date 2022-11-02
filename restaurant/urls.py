from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.viewscrud import DishesCRUD, PortionsCRUD, WaitersCRUD, RoomsCRUD, TablesCRUD, OrdersCRUD, AddressesCRUD, \
    UserCRUD, ReservationsCRUD, CouriersCRUD, DeliveryCRUD
from .views.viewsorder import place_order, add_dish

router = DefaultRouter()

router.register(r'dishes', DishesCRUD)
router.register(r'portions', PortionsCRUD)
router.register(r'waiters', WaitersCRUD)
router.register(r'rooms', RoomsCRUD)
router.register(r'tables', TablesCRUD)
router.register(r'orders', OrdersCRUD)
router.register(r'addresses', AddressesCRUD)
router.register(r'user', UserCRUD)
router.register(r'reservations', ReservationsCRUD)
router.register(r'couriers', CouriersCRUD)
router.register(r'delivery', DeliveryCRUD)


urlpatterns = [
    path("", include(router.urls)),
    path('place-order/', place_order),
    path('add-dish/', add_dish)
]
