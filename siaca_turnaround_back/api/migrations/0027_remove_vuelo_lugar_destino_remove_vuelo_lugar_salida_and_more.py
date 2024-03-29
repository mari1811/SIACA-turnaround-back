# Generated by Django 4.2.2 on 2023-09-14 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_vuelo_lugar_destino_remove_vuelo_lugar_salida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelo',
            name='lugar_destino',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='lugar_salida',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='stn',
        ),
        migrations.AddField(
            model_name='vuelo',
            name='lugar_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades_destino'),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='lugar_salida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades_salida'),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='stn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades'),
        ),
    ]
