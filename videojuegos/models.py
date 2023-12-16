from django.db import models
from django.urls import reverse
from django.conf import settings
import uuid

# Create your models here.
class Videojuego(models.Model):
	uuid = models.UUIDField (
		primary_key=True,
		db_index=True,
		default=uuid.uuid4,
		editable=False,
	)
	titulo = models.CharField(max_length=80)
	desarrolladora = models.CharField(max_length=50)
	plataformas = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	descripcion = models.CharField(max_length=1000)
	portada = models.ImageField(upload_to='portadas/', blank=True)

	class Meta:
		indexes = [
			models.Index(fields=['uuid'], name='id_index'),
		]
		# permissions = [
		# 	('special_status', 'Puede ver los juegos')
		# ]

	def __str__(self):
		return self.titulo
	
	def get_absolute_url(self):
		return reverse("detalle_videojuego", args=[str(self.uuid)])
	

class Comentario(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("lista_videojuegos")