# Generated by Django 2.2.5 on 2019-09-20 02:47

from django.db import migrations, models
import django.db.models.deletion
import movimientos.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_mi_perfil'),
        ('movimientos', '0003_material_asignado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material_asignado',
            options={'verbose_name': 'Material Asignado', 'verbose_name_plural': 'Materiales Asignados'},
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id_no', models.CharField(default=movimientos.models.get_rand_string_dev, help_text='Se asignara automaticamente un ID', max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Dato o No. de Referencia')),
                ('fecha', models.DateField(auto_now_add=True, help_text='Se tomara la fecha automatica de creacion', verbose_name='Fecha')),
                ('hora', models.TimeField(auto_now_add=True, help_text='Se tomara la fecha automatica de creacion', verbose_name='Hora')),
                ('module', models.CharField(max_length=50, verbose_name='Modulo')),
                ('estado', models.BooleanField(default=False, verbose_name='Estado')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Send_Dev', to='registration.Perfil', verbose_name='Asignado a')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Create_Dev', to='registration.Perfil', verbose_name='Creado Por')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
    ]