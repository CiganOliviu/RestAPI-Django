# Generated by Django 3.1.7 on 2021-04-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0014_auto_20210409_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='regions',
        ),
        migrations.RemoveField(
            model_name='region',
            name='locations',
        ),
        migrations.AddField(
            model_name='location',
            name='regions',
            field=models.ManyToManyField(to='rest_api.Region'),
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ManyToManyField(to='rest_api.Country'),
        ),
    ]