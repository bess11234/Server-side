# Generated by Django 5.1 on 2024-08-26 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('room_types', models.ManyToManyField(blank=True, related_name='rooms', to='bookings.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('purpose', models.CharField(blank=True, max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.room')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.staff')),
            ],
        ),
    ]
