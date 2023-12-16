from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from django.urls import reverse
from .models import Videojuego
from .forms import FormularioComentario

# Create your views here.
class VistaListaVideojuegos(ListView):
    model = Videojuego
    context_object_name = 'lista_videojuegos'
    template_name = 'videojuegos/lista_videojuegos.html'


# class VistaDetalleVideojuego(DetailView):
#     model = Videojuego
#     context_object_name = 'videojuego'
#     template_name = 'videojuegos/detalle_videojuego.html'

#     def get(self, request, *args, **kwargs):
#         view = ComentarioGet.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = ComentariosPost.as_view()
#         return view(request, *args, **kwargs)
class VistaDetalleVideojuego(View):
    def get(self, request, *args, **kwargs):
        view = ComentarioGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ComentariosPost.as_view()
        return view(request, *args, **kwargs)
    
class VistaResultadoBusqueda(ListView):
    model = Videojuego
    context_object_name = 'lista_videojuegos'
    template_name = 'videojuegos/resultado_busqueda.html'

    def get_queryset(self):
        consulta = self.request.GET.get('q')
        return Videojuego.objects.filter(
            Q(titulo__icontains=consulta)
        )


class ComentarioGet(DetailView):
    model = Videojuego
    template_name = 'videojuegos/detalle_videojuego.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioComentario()
        return context


class ComentariosPost(SingleObjectMixin, FormView, View):
    model = Videojuego
    form_class = FormularioComentario
    template_name = "videojuegos/detalle_videojuego.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.videojuego = self.object
        #form.instance.autor = self.request.user
        comentario.autor = self.request.user
        comentario.save()
        return super().form_valid(form)

    def get_success_url(self):
        videojuego = self.get_object()
        # return reverse('detalle_videojuego', args=[str(self.uuid)])
        return reverse('detalle_videojuego', kwargs={'pk':videojuego.pk})
