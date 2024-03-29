# Generated by Django 2.2.7 on 2019-11-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_timestamp', models.DateTimeField()),
                ('log_type', models.CharField(max_length=20)),
                ('source_ip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Access_Arguments',
            fields=[
                ('access_arguments_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='logdbapp.Log')),
                ('access_arguments_user_id', models.CharField(max_length=50)),
                ('access_arguments_http_method', models.CharField(max_length=20)),
                ('access_arguments_resource', models.TextField()),
                ('access_arguments_response', models.IntegerField()),
                ('access_arguments_size', models.IntegerField()),
                ('access_arguments_referer', models.TextField()),
                ('access_arguments_agent_string', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dataxceiver_Arguments',
            fields=[
                ('dataxceiver_arguments_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='logdbapp.Log')),
                ('dataxceiver_arguments_block_id', models.CharField(max_length=50)),
                ('dataxceiver_arguments_dest_ip', models.CharField(max_length=50)),
                ('dataxceiver_arguments_size', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Namesystem_Destinations',
            fields=[
                ('namesystem_destinations_id', models.AutoField(primary_key=True, serialize=False)),
                ('namesystem_destinations', models.CharField(max_length=50)),
                ('namesystem_destinations_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logdbapp.Log')),
            ],
        ),
        migrations.CreateModel(
            name='Namesystem_Blocks',
            fields=[
                ('namesystem_blocks_id', models.AutoField(primary_key=True, serialize=False)),
                ('namesystem_blocks_block_id', models.CharField(max_length=50)),
                ('namesystem_blocks_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logdbapp.Log')),
            ],
        ),
    ]
