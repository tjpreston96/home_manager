# Generated by Django 4.0.4 on 2022-05-29 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ['id']},
        ),
    ]