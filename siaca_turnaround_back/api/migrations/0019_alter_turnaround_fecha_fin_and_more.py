# Generated by Django 4.2.2 on 2023-09-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_turnaround_hora_fin_turnaround_hora_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnaround',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turnaround',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
