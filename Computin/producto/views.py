from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Producto
from . models import Compra
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
        context={'num_Productos': num_Productos,'num_Prod_Disp': num_Prod_Disp, 'num_Prod' : num_Prod, 
        'DestacadoProd' : DestacadoProd, 'OfertaProd' : OfertaProd, 'PopularProd' : PopularProd}
    )


# Create your views here. 

def ofertas(request):
    DestacadoProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Destacados') #icontains sirve para buscar entre mayus y minus
    OfertaProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Ofertas') 
    PopularProd = Producto.objects.all().filter(CategoriaEsp__icontains = 'Populares') 
    return render(
        request,
        'ofertas.html',
        context= {'DestacadoProd' : DestacadoProd, 
        'OfertaProd' : OfertaProd, 'PopularProd' : PopularProd},
    )

def comprar(request,id):
    idprod = id
    return render(
        request,
        'comprar.html',{'idprod':idprod,},
    )



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductosListView(generic.ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto

class ProcutoUpdate(UpdateView):
    model = Producto
    fields = 'StockProd'

class CompraCreate(CreateView):
    model = Compra
    fields = '__all__'

class CompraDetailView(generic.DetailView):
    model = Compra
