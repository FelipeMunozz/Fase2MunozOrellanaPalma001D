from django.test import TestCase
from producto.models import Producto , Compra

class ProductoTestCase(TestCase):

    def setUp(self):
        
        Producto.objects.create(idProd = "100", NombreProd = "placa madre 100 test")


    def test_producto_compra(self):

        producto = Producto.objects.get(idProd = "100")
        self.assertEqual(producto.NombreProd , "placa madre 100 test")






