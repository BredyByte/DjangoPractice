
import re
from tkinter import N
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from . import views

from goods.models import Categories, Products

def catalog(request):
	products = Products.objects.all()

	context = {
		'title': 'Catalog',
		'description': 'This page is about bla bla, and other blabla blog',
		'products': products
	}

	return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
	product = Products.objects.get(slug=product_slug)

	context = {
		'product': product
	}

	return render(request, 'goods/product.html', context)
