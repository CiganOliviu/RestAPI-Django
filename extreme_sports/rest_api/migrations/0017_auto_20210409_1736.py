# Generated by Django 3.1.7 on 2021-04-09 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0016_auto_20210409_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extremesport',
            old_name='country',
            new_name='place',
        ),
    ]
