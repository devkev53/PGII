# Generated by Django 2.2.5 on 2019-10-03 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20191003_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['nombre'], 'verbose_name': 'Material o Insumo', 'verbose_name_plural': 'Materiales o Insumos'},
        ),
    ]