# Generated by Django 2.2.5 on 2019-11-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_equipo_for_asig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo_for_asig',
            options={'verbose_name': 'Detalle de Equipo', 'verbose_name_plural': 'Detalle de Equipos'},
        ),
        migrations.AlterField(
            model_name='equipo_ingreso',
            name='ubicacion',
            field=models.CharField(max_length=75, verbose_name='Ubicacion'),
        ),
        migrations.AlterField(
            model_name='material_detalle',
            name='ubicacion',
            field=models.CharField(max_length=75, verbose_name='Ubicacion'),
        ),
    ]