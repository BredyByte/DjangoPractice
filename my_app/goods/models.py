from django.db import models

class Categories(models.Model):
	name = models.CharField(max_length=150, unique=True, verbose_name='Titulo')
	slug: int = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

	class Meta:
		db_table = 'category'
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'

	def __str__(self):
		return self.name


class Products(models.Model):
	MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
	medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10, verbose_name='Tipo de valor')
	name = models.CharField(
		help_text="Poner el nombre así y sólo como está escrito en el artículo",
		max_length=150,
		unique=True,
		verbose_name='Titulo',
	)
	slug: int = models.SlugField(
		max_length=200,
		unique=True,
		blank=True,
		null=True,
		verbose_name='URL'
	)
	description = models.TextField(blank=True, null=True, verbose_name='Descripción', default="https://www.pornhub.com/information/terms#faq")
	image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Imagen')
	price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Precio')
	discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Descuento en %')
	quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad de stock')
	category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Categoría')

	class Meta:
		db_table = 'product'
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

	# When creating a row using this class, it appears as 'Object1' in the Admin panel.
	# This function modifies that behavior.
	def __str__(self):
		return f'{self.name} Cantidad - {self.quantity}'
