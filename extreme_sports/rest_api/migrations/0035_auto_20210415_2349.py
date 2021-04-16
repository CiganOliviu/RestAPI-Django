# Generated by Django 3.1.7 on 2021-04-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0034_auto_20210415_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extremesport',
            name='end_of_season',
        ),
        migrations.RemoveField(
            model_name='extremesport',
            name='start_of_season',
        ),
        migrations.AddField(
            model_name='extremesport',
            name='period',
            field=models.CharField(default='', max_length=100),
        ),
    ]
