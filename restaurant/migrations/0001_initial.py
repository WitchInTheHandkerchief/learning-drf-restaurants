# Generated by Django 4.1.2 on 2022-10-31 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30, verbose_name='Street name')),
                ('house', models.CharField(max_length=20, verbose_name='House number')),
                ('apartment', models.CharField(blank=True, max_length=10, null=True, verbose_name='Apartment number')),
                ('block', models.CharField(blank=True, max_length=10, null=True, verbose_name='Block number')),
                ('floor', models.PositiveIntegerField(blank=True, null=True, verbose_name='Floor number')),
            ],
            options={
                'db_table': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Couriers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('transport', models.CharField(choices=[('bicycle', 'bicycle'), ('walking', 'walking'), ('motorcycle', 'motorcycle'), ('car', 'car')], default='bicycle', max_length=20, verbose_name='Transport')),
                ('is_free', models.BooleanField(default=True, verbose_name='Is free')),
            ],
            options={
                'db_table': 'Couriers',
            },
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Room name')),
            ],
            options={
                'db_table': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Waiters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('number', models.PositiveBigIntegerField(verbose_name='Phone number')),
            ],
            options={
                'db_table': 'Waiters',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('address', models.ManyToManyField(blank=True, to='restaurant.addresses')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Table number')),
                ('is_free', models.BooleanField(default=True, verbose_name='Is free')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.rooms')),
            ],
            options={
                'db_table': 'Tables',
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End date')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.tables')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.user')),
            ],
            options={
                'db_table': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='Portions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20, verbose_name='Amount')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.dishes')),
            ],
            options={
                'db_table': 'Portions',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End date')),
                ('total', models.PositiveIntegerField(verbose_name='Total sum')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('with_delivery', models.BooleanField(default=False, verbose_name='With delivery')),
                ('dishes', models.ManyToManyField(to='restaurant.dishes')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.tables')),
                ('waiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.waiters')),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('cooking', 'cooking'), ('delivering', 'delivering'), ('arrived', 'arrived')], default='cooking', max_length=20, verbose_name='Status')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Start time')),
                ('recieved_time', models.DateTimeField(verbose_name='Recieved time')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.addresses')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.couriers')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.user')),
            ],
            options={
                'db_table': 'Delivery',
            },
        ),
    ]
