# Generated by Django 3.1.5 on 2022-06-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20220622_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]
