# Generated by Django 4.1.1 on 2022-09-05 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]