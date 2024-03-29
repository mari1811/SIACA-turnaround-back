# Generated by Django 4.2.2 on 2023-09-25 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_ciudades_aeropuerto'),
    ]

    operations = [
        migrations.CreateModel(
            name='maquinaria_historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateField(blank=True, null=True)),
                ('hora_fin', models.DateField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('fk_maquinaria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.maquinaria')),
            ],
        ),
    ]
