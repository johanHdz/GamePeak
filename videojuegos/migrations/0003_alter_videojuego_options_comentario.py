# Generated by Django 4.0.10 on 2023-12-15 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videojuegos', '0002_alter_videojuego_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videojuego',
            options={},
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videojuegos.videojuego')),
            ],
        ),
    ]