from .views import VistaListaVideojuegos, VistaDetalleVideojuego, VistaResultadoBusqueda
from django.urls import path

urlpatterns = [
path('', VistaListaVideojuegos.as_view(), name='lista_videojuegos'),
path('<uuid:pk>/', VistaDetalleVideojuego.as_view(), name='detalle_videojuego'),
path('buscar/', VistaResultadoBusqueda.as_view(), name='resultado_busqueda'),
]