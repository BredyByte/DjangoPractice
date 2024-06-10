
import re
from tkinter import N
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from . import views

from goods.models import Categories, Products

def catalog(request):
	products = Products.objects.all()

	modified_products = []

	for product in products:
		discount = product.discount
		if discount:
			discounted_price = product.price - (product.price * discount / 100)
			product.discount_price = discounted_price
		modified_products.append(product)

	context = {
		'title': 'Catalog',
		'description': 'This page is about bla bla, and other blabla blog',
		'products': modified_products
	}

	return render(request, 'goods/catalog.html', context)

class MyTestView(generic.ListView):
	template_name = "goods/testPage.html"
	context_object_name = "categ_list"

	def get_queryset(self):
		return Categories.objects.all()


def product(request):
	return render(request, 'goods/product.html')
