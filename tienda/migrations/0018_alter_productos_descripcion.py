# Generated by Django 4.2 on 2023-06-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0017_agengar_horas_disponibles_carro_carrucel_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(),
        ),
    ]