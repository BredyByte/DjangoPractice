import re
from django.http import HttpResponse
from django.shortcuts import render

def get_footer_data():
	copyright = 'Copyright &copy; Home Python Hub Studio 2023'
	return copyright

def get_index_context():
	context = {
		'title': 'Home Page',
		'context': 'TheShoP: main page HOME',
		'footer_text': get_footer_data()
	}
	return context

def get_about_context():
	context = {
		'title': 'About Page',
		'context': 'TheShoP: About page here!!',
		'footer_text': get_footer_data(),
		'text_on_page': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore vero laudantium quaerat in odit? Sapiente, saepe! Suscipit dolores ducimus odit quae necessitatibus, neque hic cumque exercitationem, ut corrupti, minima saepe!'
	}
	return context;

def index(request):
	return render(request, 'main/index.html', get_index_context())

def about(request):
	return render(request, 'main/about.html', get_about_context())
