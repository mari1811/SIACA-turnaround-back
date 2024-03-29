# Generated by Django 4.2.2 on 2023-08-23 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_maquinaria_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ciudades_destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ciudades_salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='ATA',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='ATD',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='ETA',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='ETD',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='vuelo',
            name='stn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='lugar_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades_destino'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='lugar_salida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudades_salida'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='tipo_vuelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tipo_vuelo'),
        ),
    ]
