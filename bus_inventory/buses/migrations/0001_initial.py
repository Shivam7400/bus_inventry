# Generated by Django 5.0 on 2024-02-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('trip', models.CharField(max_length=255)),
                ('trip_duration', models.DurationField()),
                ('conductor', models.CharField(max_length=100)),
                ('driver', models.CharField(max_length=100)),
            ],
        ),
    ]