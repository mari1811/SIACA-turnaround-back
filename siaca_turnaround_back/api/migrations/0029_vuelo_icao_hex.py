# Generated by Django 4.2.2 on 2023-09-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_vuelo_lugar_destino_alter_vuelo_lugar_salida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vuelo',
            name='icao_hex',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
