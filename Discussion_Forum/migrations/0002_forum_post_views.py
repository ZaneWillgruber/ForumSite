# Generated by Django 3.2.6 on 2021-09-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_Forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='post_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]