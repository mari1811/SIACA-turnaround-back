# Generated by Django 4.2.2 on 2024-02-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_remove_imagen_link_imagen_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerolinea',
            name='codigo_OACI',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aerolinea',
            name='codigo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]