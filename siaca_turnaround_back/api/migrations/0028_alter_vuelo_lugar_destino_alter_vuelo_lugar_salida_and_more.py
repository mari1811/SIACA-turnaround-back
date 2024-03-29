# Generated by Django 4.2.2 on 2023-09-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_remove_vuelo_lugar_destino_remove_vuelo_lugar_salida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='lugar_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudades_destino', to='api.ciudades'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='lugar_salida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudades_salida', to='api.ciudades'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='stn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudades_stn', to='api.ciudades'),
        ),
        migrations.DeleteModel(
            name='ciudades_destino',
        ),
        migrations.DeleteModel(
            name='ciudades_salida',
        ),
    ]
