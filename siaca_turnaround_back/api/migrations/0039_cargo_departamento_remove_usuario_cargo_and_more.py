# Generated by Django 4.2.2 on 2023-10-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_alter_comentario_comentario_alter_hora_hora_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='departamento',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fk_cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cargo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fk_departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.departamento'),
        ),
    ]
