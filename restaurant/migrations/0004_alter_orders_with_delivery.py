# Generated by Django 4.1.2 on 2022-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_orders_with_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='with_delivery',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='With delivery'),
        ),
    ]
