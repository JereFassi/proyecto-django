# Generated by Django 3.2.18 on 2023-05-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_baja',
            field=models.DateField(blank=True, default=None, verbose_name='Fecha de Baja'),
        ),
    ]
