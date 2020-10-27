from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('comprar', views.comprar, name='comprar'),
    path('productos/', views.ProductosListView.as_view(), name='productos'),
    path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),

    
]