from django.db import models
from django.urls import reverse # Se utiliza para direccionar los path de nmuestro proyecto asociado al modelo
import uuid # Se utiliza para relacionar objetos de de Instancia de productos

# Create your models here.
#save() = insert
#object.all = select *
#objects.all.filter() = select -- where 


# Create your models here.
class Producto(models.Model):
	idProd = models.IntegerField(null=True)
	NombreProd = models.CharField(max_length=150)
	MarcaProd = models.CharField(max_length=150)
	PrecioProd = models.IntegerField(null=True)
	StockProd = models.IntegerField(null=True)
	DescripciónProd = models.TextField(max_length=5000)

	def __str__(self):
		return self.NombreProd
