# Generated by Django 2.2.5 on 2019-09-15 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Perfil', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Mi Tarjeta de Responsabilidad',
                'verbose_name_plural': 'Tarjetas de Responsabilidad',
            },
        ),
    ]