# Generated by Django 3.1.5 on 2022-06-22 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_bill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopping',
            options={'ordering': ['item']},
        ),
    ]
