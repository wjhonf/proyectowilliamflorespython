# Generated by Django 5.0.2 on 2024-03-11 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appventas', '0007_detalleventa_venta_detalleventa_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='equipos',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='DetalleVenta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]