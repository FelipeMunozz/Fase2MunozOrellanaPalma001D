# Generated by Django 3.1.2 on 2020-10-19 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_remove_producto_categoriaesp'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='CategoriaEsp',
            field=models.CharField(default=django.utils.timezone.now, help_text='Categorias especiales (Destacados,Ofertas,Populares).Dejar vacio sino posee ', max_length=150),
            preserve_default=False,
        ),
    ]