# Generated by Django 4.2.4 on 2024-01-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_alter_ratingseller_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingseller',
            name='total_average_rating',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='overall_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]