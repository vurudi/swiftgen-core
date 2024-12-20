# Generated by Django 4.2.4 on 2024-07-24 08:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleOverview', models.CharField(max_length=100)),
                ('overall_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('search_tags', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StandardPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Standard_title', models.CharField(default='', max_length=100)),
                ('Standard_description', models.TextField(default='')),
                ('Standard_delivery_time', models.PositiveIntegerField(choices=[(1, '1 days'), (2, '2 days'), (3, '3 days'), (4, '4 days'), (5, '5 days'), (6, '6 days'), (7, '7 days'), (8, '8 days'), (9, '9 days'), (10, '10 days'), (11, '11 days'), (12, '12 days'), (13, '13 days'), (14, '14 days'), (15, '15 days'), (16, '16 days'), (17, '17 days'), (18, '18 days'), (19, '19 days'), (20, '20 days'), (21, '21 days'), (22, '22 days'), (23, '23 days'), (24, '24 days'), (25, '25 days'), (26, '26 days'), (27, '27 days'), (28, '28 days'), (29, '29 days'), (30, '30 days'), (31, '31 days'), (32, '32 days'), (33, '33 days'), (34, '34 days'), (35, '35 days'), (36, '36 days'), (37, '37 days'), (38, '38 days'), (39, '39 days'), (40, '40 days'), (41, '41 days'), (42, '42 days'), (43, '43 days'), (44, '44 days'), (45, '45 days'), (46, '46 days'), (47, '47 days'), (48, '48 days'), (49, '49 days'), (50, '50 days'), (51, '51 days'), (52, '52 days'), (53, '53 days'), (54, '54 days'), (55, '55 days'), (56, '56 days'), (57, '57 days'), (58, '58 days'), (59, '59 days'), (60, '60 days'), (61, '61 days'), (62, '62 days'), (63, '63 days'), (64, '64 days'), (65, '65 days'), (66, '66 days'), (67, '67 days'), (68, '68 days'), (69, '69 days'), (70, '70 days'), (71, '71 days'), (72, '72 days'), (73, '73 days'), (74, '74 days'), (75, '75 days'), (76, '76 days'), (77, '77 days'), (78, '78 days'), (79, '79 days'), (80, '80 days'), (81, '81 days'), (82, '82 days'), (83, '83 days'), (84, '84 days'), (85, '85 days'), (86, '86 days'), (87, '87 days'), (88, '88 days'), (89, '89 days'), (90, '90 days')], default=1)),
                ('Standard_revisions', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), ('unlimited', 'unlimited')], default=1)),
                ('Standard_source_file', models.BooleanField(default=False)),
                ('Standard_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(100)])),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='', max_length=200)),
                ('question_type', models.CharField(choices=[('text', 'Text Answer'), ('textarea', 'Text Area'), ('choices', 'Multiple Choice')], max_length=20)),
                ('text', models.TextField(default='', max_length=200)),
                ('choices', models.CharField(default='', max_length=10)),
                ('allow_multiple_selection', models.BooleanField(default=False)),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='PremiumPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Premium_title', models.CharField(default='', max_length=100)),
                ('Premium_description', models.TextField(default='')),
                ('Premium_delivery_time', models.PositiveIntegerField(choices=[(1, '1 days'), (2, '2 days'), (3, '3 days'), (4, '4 days'), (5, '5 days'), (6, '6 days'), (7, '7 days'), (8, '8 days'), (9, '9 days'), (10, '10 days'), (11, '11 days'), (12, '12 days'), (13, '13 days'), (14, '14 days'), (15, '15 days'), (16, '16 days'), (17, '17 days'), (18, '18 days'), (19, '19 days'), (20, '20 days'), (21, '21 days'), (22, '22 days'), (23, '23 days'), (24, '24 days'), (25, '25 days'), (26, '26 days'), (27, '27 days'), (28, '28 days'), (29, '29 days'), (30, '30 days'), (31, '31 days'), (32, '32 days'), (33, '33 days'), (34, '34 days'), (35, '35 days'), (36, '36 days'), (37, '37 days'), (38, '38 days'), (39, '39 days'), (40, '40 days'), (41, '41 days'), (42, '42 days'), (43, '43 days'), (44, '44 days'), (45, '45 days'), (46, '46 days'), (47, '47 days'), (48, '48 days'), (49, '49 days'), (50, '50 days'), (51, '51 days'), (52, '52 days'), (53, '53 days'), (54, '54 days'), (55, '55 days'), (56, '56 days'), (57, '57 days'), (58, '58 days'), (59, '59 days'), (60, '60 days'), (61, '61 days'), (62, '62 days'), (63, '63 days'), (64, '64 days'), (65, '65 days'), (66, '66 days'), (67, '67 days'), (68, '68 days'), (69, '69 days'), (70, '70 days'), (71, '71 days'), (72, '72 days'), (73, '73 days'), (74, '74 days'), (75, '75 days'), (76, '76 days'), (77, '77 days'), (78, '78 days'), (79, '79 days'), (80, '80 days'), (81, '81 days'), (82, '82 days'), (83, '83 days'), (84, '84 days'), (85, '85 days'), (86, '86 days'), (87, '87 days'), (88, '88 days'), (89, '89 days'), (90, '90 days')], default=1)),
                ('Premium_revisions', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), ('unlimited', 'unlimited')], default=1)),
                ('Premium_source_file', models.BooleanField(default=False)),
                ('Premium_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(150)])),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='BasicPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basic_title', models.CharField(default='', max_length=100)),
                ('Basic_description', models.TextField(default='')),
                ('Basic_delivery_time', models.PositiveIntegerField(choices=[(1, '1 days'), (2, '2 days'), (3, '3 days'), (4, '4 days'), (5, '5 days'), (6, '6 days'), (7, '7 days'), (8, '8 days'), (9, '9 days'), (10, '10 days'), (11, '11 days'), (12, '12 days'), (13, '13 days'), (14, '14 days'), (15, '15 days'), (16, '16 days'), (17, '17 days'), (18, '18 days'), (19, '19 days'), (20, '20 days'), (21, '21 days'), (22, '22 days'), (23, '23 days'), (24, '24 days'), (25, '25 days'), (26, '26 days'), (27, '27 days'), (28, '28 days'), (29, '29 days'), (30, '30 days'), (31, '31 days'), (32, '32 days'), (33, '33 days'), (34, '34 days'), (35, '35 days'), (36, '36 days'), (37, '37 days'), (38, '38 days'), (39, '39 days'), (40, '40 days'), (41, '41 days'), (42, '42 days'), (43, '43 days'), (44, '44 days'), (45, '45 days'), (46, '46 days'), (47, '47 days'), (48, '48 days'), (49, '49 days'), (50, '50 days'), (51, '51 days'), (52, '52 days'), (53, '53 days'), (54, '54 days'), (55, '55 days'), (56, '56 days'), (57, '57 days'), (58, '58 days'), (59, '59 days'), (60, '60 days'), (61, '61 days'), (62, '62 days'), (63, '63 days'), (64, '64 days'), (65, '65 days'), (66, '66 days'), (67, '67 days'), (68, '68 days'), (69, '69 days'), (70, '70 days'), (71, '71 days'), (72, '72 days'), (73, '73 days'), (74, '74 days'), (75, '75 days'), (76, '76 days'), (77, '77 days'), (78, '78 days'), (79, '79 days'), (80, '80 days'), (81, '81 days'), (82, '82 days'), (83, '83 days'), (84, '84 days'), (85, '85 days'), (86, '86 days'), (87, '87 days'), (88, '88 days'), (89, '89 days'), (90, '90 days')], default=1)),
                ('Basic_revisions', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), ('unlimited', 'unlimited')], default=1)),
                ('Basic_source_file', models.BooleanField(default=False)),
                ('Basic_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(50)])),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
            ],
        ),
        migrations.CreateModel(
            name='RatingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('title', models.CharField(max_length=50)),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('overview', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Services.overview')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_giver_service', to='Home.userprofile')),
            ],
            options={
                'unique_together': {('overview', 'reviewer')},
            },
        ),
    ]
