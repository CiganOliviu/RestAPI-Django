# Generated by Django 3.1.7 on 2021-04-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0011_country_extremesport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extremesport',
            name='country',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api.country'),
        ),
    ]
