# Generated by Django 4.2.2 on 2023-08-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_vuelo_eta_alter_vuelo_etd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelo',
            name='fecha_llegada',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='hora_llegada',
        ),
    ]
