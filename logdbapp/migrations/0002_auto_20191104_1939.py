# Generated by Django 2.2.7 on 2019-11-04 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logdbapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='namesystem_destinations',
            old_name='namesystem_destinations',
            new_name='namesystem_destinations_dest_ip',
        ),
    ]
