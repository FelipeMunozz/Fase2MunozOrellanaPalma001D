from django.db import models
from django.urls import reverse # Se utiliza para direccionar los path de nmuestro proyecto asociado al modelo
import uuid # Se utiliza para relacionar objetos de de Instancia de productos

# Create your models here.
class Producto(models.Model):
	idProd = models.IntegerField(primary_key=True,help_text='Id única del producto')
	NombreProd = models.CharField(max_length=150)
	MarcaProd = models.CharField(max_length=150)
	CategoriaProd = models.CharField(max_length=150,null=True)
	CategoriaEsp = models.CharField(max_length=150,null=True,help_text='Categorias especiales (Destacados,Ofertas,Populares).Sino posee dejar como "Ninguno"')
	PrecioProd = models.IntegerField(null=True)
	StockProd = models.IntegerField(null=True)
	imageProd = models.ImageField(upload_to='imagesProd/', null=True, blank=True)
	DescripciónProd = models.TextField(max_length=5000)

	def __str__(self):
		return self.NombreProd
