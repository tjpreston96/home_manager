# Generated by Django 4.0.4 on 2022-05-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_plant_watering frequency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='Watering Frequency',
            new_name='watering_frequency',
        ),
    ]
