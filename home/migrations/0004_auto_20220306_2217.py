# Generated by Django 3.2.12 on 2022-03-06 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_trip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='vehicle_id',
            new_name='vehicle',
        ),
    ]