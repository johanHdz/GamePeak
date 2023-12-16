from django.contrib import admin
from .models import Videojuego, Comentario

class ComentarioEnLinea(admin.TabularInline):
    model = Comentario
    extra = 0

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo','desarrolladora','plataformas','precio','descripcion')
    inlines = [
        ComentarioEnLinea,
    ]
     
# Register your models here.	
admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Comentario)
