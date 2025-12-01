from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Listado principal del blog
    path('', views.ArticuloListView.as_view(), name='listado'),
    # Detalle del artículo usando slug
    path('<slug:slug>/', views.ArticuloDetailView.as_view(), name='detalle'),
]