# Generated by Django 2.2.5 on 2019-09-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20190903_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Catalogo/', verbose_name='Imagen'),
        ),
    ]