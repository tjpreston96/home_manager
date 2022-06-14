# Generated by Django 4.0.4 on 2022-05-29 15:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('light', models.CharField(choices=[('Shade', 'Shade'), ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Full Sun', 'Full Sun')], default='Low', max_length=10)),
                ('toxicity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('environment', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], default='Indoor', max_length=7)),
                ('Watering Frequency', models.IntegerField(choices=[(1, 'Daily'), (3, 'Biweekly'), (7, 'Weekly'), (14, 'Two Weeks'), (21, 'Three Weeks'), (30, 'Monthly')])),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('nutrients', models.CharField(choices=[('W', 'Water'), ('F', 'Nutrient Foam')], max_length=20)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]