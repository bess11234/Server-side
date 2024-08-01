# Generated by Django 5.0.7 on 2024-07-27 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.TextField()),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.store')),
            ],
        ),
    ]
