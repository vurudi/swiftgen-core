# Generated by Django 4.2.4 on 2023-09-01 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0010_rename_delivery_time_basicpackage_basic_delivery_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpackage',
            name='Basic_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='premiumpackage',
            name='Premium_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='standardpackage',
            name='Standard_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(100)]),
        ),
    ]
