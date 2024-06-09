import re
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):
	categories = Categories.objects.all()

	context = {
		'title': 'Home Page',
		'context': 'TheShoP: main page HOME',
		'categories': categories
	}

	return render(request, 'main/index.html', context)

def about(request):
	context = {
		'title': 'About Page',
		'context': 'TheShoP: About page here!!',
		'text_on_page': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore vero laudantium quaerat in odit? Sapiente, saepe! Suscipit dolores ducimus odit quae necessitatibus, neque hic cumque exercitationem, ut corrupti, minima saepe!'
	}

	return render(request, 'main/about.html', context)
