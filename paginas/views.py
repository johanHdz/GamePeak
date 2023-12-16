from django.views.generic import TemplateView

# Create your views here.
class VistaPaginaInicio(TemplateView):
    template_name = 'inicio.html'

class VistaAcercaDe(TemplateView):
    template_name = 'acercade.html'