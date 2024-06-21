from django.contrib import admin
from users.models import User
from carts.admin import CartTabAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'last_name', 'email']
	search_fields = ['username', 'first_name', 'last_name', 'email']

	# Подвязка инлайновой формы корзин к каждому пользователю
	# Чтобы в панеле админа юзеров было видно так же их корзины (на личной странице пользователя).
	inlines = [CartTabAdmin]

# Простой способ, без кастомизации
# admin.site.register(User)

