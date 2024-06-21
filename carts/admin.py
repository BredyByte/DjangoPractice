from django.contrib import admin

from carts.models import Cart

# Подвязка карзин к пользователям. В admin.py есть дополнение
# к этому коду, чтобы в админ пане это отображалось.
class CartTabAdmin(admin.TabularInline):
	model = Cart
	fields = ['product', 'quantity', 'created_timestamp']
	search_fields = ['product', 'quantity', 'created_timestamp']
	readonly_fields = ('created_timestamp', )
	extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	"""
	где пишу __name я хочу взять только имя,
	такf как мы изменили его в models.py
	и теперь выдает то что написано в __str__  методе.
	В случае с продуктовым название, почему не работает, так что я просто создал снизу функцию.
	"""
	list_display = ['user', 'display_product_name', 'quantity', 'created_timestamp']
	list_filter = ['created_timestamp', 'user', 'product__name']

	def display_product_name(self, obj):
		return str(obj.product.name)
