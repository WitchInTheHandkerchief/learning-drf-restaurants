from django.contrib import admin
from .models import Dishes, Waiters, Portions, Rooms, Tables, Orders, Addresses, Reservations, User, Couriers, Delivery

# Register your models here.

admin.site.register(Dishes)
admin.site.register(Portions)
admin.site.register(Waiters)
admin.site.register(Rooms)
admin.site.register(Tables)
admin.site.register(Orders)
admin.site.register(Addresses)
admin.site.register(User)
admin.site.register(Reservations)
admin.site.register(Couriers)
admin.site.register(Delivery)