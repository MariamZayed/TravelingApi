# Generated by Django 3.2.12 on 2022-03-02 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_vehicle_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='available_seat',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='license_plate',
        ),
    ]