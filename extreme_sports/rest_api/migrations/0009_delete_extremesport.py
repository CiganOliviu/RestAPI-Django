# Generated by Django 3.1.7 on 2021-04-09 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0008_remove_extremesport_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExtremeSport',
        ),
    ]