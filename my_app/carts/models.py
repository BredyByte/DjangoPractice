from django.db import models
from goods.models import Products
from users.models import User


#Таки образом в файле included_cart.html можно вызвать этот метом у обьекта
class CartQueryset(models.QuerySet):

	def total_price(self):
		return sum(cart.display_discounted_price() for cart in self)

	def total_quantity(self):
		if self:
			return sum(cart.quantity for cart in self)
		return 0


class Cart(models.Model):

	user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')
	product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Producto')
	quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Cantidad')
	session_key = models.CharField(max_length=32, null=True, blank=True)
	created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')

	class Meta:
		db_table = 'cart'
		verbose_name = 'Carito'
		verbose_name_plural = 'Carito'

	objects = CartQueryset().as_manager()

	def products_price(self):
		return round(self.product.display_discounted_price() * self.quantity, 2)

	def __str__(self):
		return f'Carito {self.user.username} | Producto {self.product.name} | Cantidad {self.quantity}'
