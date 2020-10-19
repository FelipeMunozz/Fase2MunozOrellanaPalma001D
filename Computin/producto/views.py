from django.shortcuts import render
from . models import Producto
from django.views import generic

# Create your views here.
def index(request):
    num_Productos = Producto.objects.all().count()
    num_Prod_Disp = Producto.objects.all().count()
    num_Prod = Producto.objects.all()
    DestacadoProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Destacados') #icontains sirve para buscar entre mayus y minus
    OfertaProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Ofertas') 
    PopularProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Populares') 

    return render(
        request,
        'index.html',
        context={'num_Productos': num_Productos,'num_Prod_Disp': num_Prod_Disp, 'num_Prod' : num_Prod, 'DestacadoProd' : DestacadoProd, 'OfertaProd' : OfertaProd, 'PopularProd' : PopularProd}
    )
