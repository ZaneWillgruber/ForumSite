# Generated by Django 3.2.6 on 2021-10-25 20:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
