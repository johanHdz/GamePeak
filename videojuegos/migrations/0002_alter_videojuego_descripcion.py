# Generated by Django 4.0.10 on 2023-12-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videojuegos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
    ]
