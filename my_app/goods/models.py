from django.db import models

class Categories(models.Model):
	name = models.CharField(max_length=150, unique=True, verbose_name='Titulo')
	slug: int = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

	class Meta:
		db_table = 'category'
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'


class Products(models.Model):
	name = models.CharField(max_length=150, unique=True, verbose_name='Titulo')
	slug: int = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
	description = models.TextField(blank=True, null=True, verbose_name='Descripción')
	image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Imagen')
	price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Precio')
	discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Descuento en %')
	quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad de stock')
	category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Categoría')

	class Meta:
		db_table = 'product'
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

