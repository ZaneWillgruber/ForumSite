# Generated by Django 3.2.6 on 2021-11-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='category',
            name='totalCost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='category',
            name='types',
            field=models.CharField(default='Entertainment', max_length=20),
            preserve_default=False,
        ),
    ]
