from django.db import models


# Create your models here.

class Dishes(models.Model):
    class Meta:
        db_table = 'Dishes'

    def __str__(self):
        return f'Name:{self.name}, Desc:{self.description}'

    name = models.CharField("Name", max_length=40)
    description = models.TextField("Description", null=True, blank=True)


class Portions(models.Model):
    class Meta:
        db_table = 'Portions'

    def __str__(self):
        return f'Dish:{self.dish.name}, Amount:{self.amount}, Price:{self.price}'

    amount = models.CharField('Amount', max_length=20)
    price = models.PositiveIntegerField('Price')
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)


class Waiters(models.Model):
    class Meta:
        db_table = 'Waiters'

    def __str__(self):
        return f'Name:{self.name}, Surname:{self.surname}'

    name = models.CharField('Name', max_length=30)
    surname = models.CharField('Surname', max_length=30)
    birth_date = models.DateField('Birth date')
    number = models.PositiveBigIntegerField('Phone number')


class Rooms(models.Model):
    class Meta:
        db_table = 'Rooms'

    def __str__(self):
        return f'Name:{self.name}'

    name = models.CharField('Room name', max_length=30)


class Tables(models.Model):
    class Meta:
        db_table = 'Tables'

    def __str__(self):
        return f'Number:{self.number}, Room:{self.room.name}, Is free:{self.is_free}'

    number = models.PositiveIntegerField('Table number')
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    is_free = models.BooleanField('Is free', default=True)


class Orders(models.Model):
    class Meta:
        db_table = 'Orders'

    table = models.ForeignKey(Tables, on_delete=models.CASCADE, null=True, blank=True)
    dishes = models.ManyToManyField(Dishes)
    start_date = models.DateTimeField('Start date', auto_now_add=True)
    end_date = models.DateTimeField('End date', null=True, blank=True)
    total = models.PositiveIntegerField('Total sum', null=True, blank=True)
    waiter = models.ForeignKey(Waiters, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField('Is active', default=True)
    with_delivery = models.BooleanField('With delivery', default=False)


class Addresses(models.Model):
    class Meta:
        db_table = 'Addresses'

    def __str__(self):
        return f'Street:{self.street}, House:{self.house}, Apartment:{self.apartment}'

    street = models.CharField('Street name', max_length=30)
    house = models.CharField('House number', max_length=20)
    apartment = models.CharField('Apartment number', max_length=10, null=True, blank=True)
    block = models.CharField('Block number', max_length=10, null=True, blank=True)
    floor = models.PositiveIntegerField('Floor number', null=True, blank=True)


class User(models.Model):
    class Meta:
        db_table = 'User'

    def __str__(self):
        return f'Name:{self.name}, Number:{self.number}'

    name = models.CharField('Name', max_length=30)
    number = models.CharField('Phone number', max_length=20)
    address = models.ManyToManyField(Addresses, blank=True)


class Reservations(models.Model):
    class Meta:
        db_table = 'Reservations'

    def __str__(self):
        return f'Table:{self.table}, Start date:{self.start_date}, End date:{self.end_date}'

    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Couriers(models.Model):
    class Meta:
        db_table = 'Couriers'

    def __str__(self):
        return f'Name:{self.name} {self.surname}, Transport:{self.transport}'

    class Transport(models.TextChoices):
        BICYCLE = 'bicycle', 'bicycle'
        WALKING = 'walking', 'walking'
        MOTORCYCLE = 'motorcycle', 'motorcycle'
        CAR = 'car', 'car'

    name = models.CharField('Name', max_length=30)
    surname = models.CharField('Surname', max_length=30)
    birth_date = models.DateField('Birth date')
    transport = models.CharField('Transport', choices=Transport.choices, max_length=20, default=Transport.BICYCLE)
    is_free = models.BooleanField('Is free', default=True)


class Delivery(models.Model):
    class Meta:
        db_table = 'Delivery'

    def __str__(self):
        return f'Courier:{self.courier.name} {self.courier.surname}, Status:{self.status}'

    class Statuses(models.TextChoices):
        COOKING = 'cooking', 'cooking'
        DELIVERING = 'delivering', 'delivering'
        ARRIVED = 'arrived', 'arrived'

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=20, choices=Statuses.choices, default=Statuses.COOKING)
    courier = models.ForeignKey(Couriers, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    recieved_time = models.DateTimeField('Recieved time')
