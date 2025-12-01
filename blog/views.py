from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articulo

# Create your views here.
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'blog/listado_articulos.html'
    context_object_name = 'articulos'
    paginate_by = 10

    def get_queryset(self):
        queryset = Articulo.objects.filter(publicado=True)
        categoria = self.request.GET.get('categoria')
        queryset = Articulo.objects.filter(publicado=True)
        
        if categoria and categoria != 'TODOS':
            return queryset.filter(categoria=categoria)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias_filtro'] = Articulo.CATEGORIA_CHOICES
        context['categoria_activa'] = self.request.GET.get('categoria', 'TODOS')
        return context


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'blog/detalle_articulo.html'
    context_object_name = 'articulo'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().filter(publicado=True)