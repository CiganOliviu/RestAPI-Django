# Generated by Django 3.1.7 on 2021-04-09 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0013_auto_20210409_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extremesport',
            name='country',
        ),
        migrations.AddField(
            model_name='extremesport',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rest_api.country'),
        ),
    ]
