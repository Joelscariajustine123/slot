# Generated by Django 5.1.5 on 2025-01-22 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_range', models.CharField(max_length=50)),
                ('days', models.CharField(max_length=100)),
                ('total_students', models.IntegerField(default=0)),
                ('system_required', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcard_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('system_required', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slot_availability.course')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slot_availability.slot')),
            ],
        ),
    ]
