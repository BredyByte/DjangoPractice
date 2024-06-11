
import re
from tkinter import N
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views import generic
from goods.models import Categories, Products

def catalog(request, category_slug):

	page = request.GET.get('page', 1)

	if category_slug == 'all':
		products = Products.objects.all()
	else:
		products = get_list_or_404( Products.objects.filter(category__slug=category_slug))

	paginator = Paginator(products, 3)
	current_page = paginator.page(int(page))

	context = {
		'title': 'Catalog',
		'description': 'This page is about bla bla, and other blabla blog',
		'products': current_page,
		'slug_url': category_slug,
	}



	return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
	product = Products.objects.get(slug=product_slug)

	context = {
		'product': product
	}

	return render(request, 'goods/product.html', context)
