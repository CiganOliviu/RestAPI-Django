# Generated by Django 3.1.7 on 2021-04-15 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0028_auto_20210415_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='extremesport',
            name='periods',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
