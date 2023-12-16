from django.urls import path
from .views import VistaPaginaInicio, VistaAcercaDe

urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name='inicio'),
    path('acercade/', VistaAcercaDe.as_view(), name='acercade'),
]