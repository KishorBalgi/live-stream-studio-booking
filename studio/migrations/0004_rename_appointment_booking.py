# Generated by Django 3.2.5 on 2022-01-23 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_rename_date_appointment_event_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='Booking',
        ),
    ]
