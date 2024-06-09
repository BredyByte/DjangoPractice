from django.urls import path
from goods import views

app_name = 'goods'
urlpatterns = [
	#path("", views.MyTestView.as_view(), name='index'), #Some of documentation tests
	path('', views.catalog, name='index'),
	path('product/', views.product, name='product'),

]
