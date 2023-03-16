# Generated by Django 4.1.7 on 2023-03-16 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dor_num', models.PositiveIntegerField()),
                ('seat_num', models.PositiveIntegerField()),
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=10)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('price', models.PositiveIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='car_photos/')),
            ],
        ),
    ]
