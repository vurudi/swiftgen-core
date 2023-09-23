# Generated by Django 4.2.4 on 2023-09-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('expired', 'Expired'), ('delivered', 'Delivered'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
