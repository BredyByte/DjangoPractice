from django.contrib import admin
from goods.models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)} # Свойство класса admin.ModelAdmin, заполняющее автоматически одно поле на основе ддругого, в данном случае слаг на основе имени.
	list_display = ['name', 'quantity', 'price', 'discount'] # Теперь в базе данных наглядно отображаются продуктов
	list_editable = ['discount'] # Теперь поле скидки можно изменять прям в админке
	search_fields = ['name', 'description'] # Появилось поле в адменки для поиска по базе
	list_filter = ('discount', 'quantity', 'category')  # Появится кнопки фильтров
	fields = [
		'name',
		'category',
		'slug',
		'description',
		'image',
		('price', 'discount'),
		'quantity'
	]
