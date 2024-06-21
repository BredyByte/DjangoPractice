from django.shortcuts import render

def index(request):
	context = {
		'title': 'Home Page',
		'context': 'TheShoP: main page HOME',
	}

	return render(request, 'main/index.html', context)

def about(request):
	context = {
		'title': 'About Page',
		'context': 'TheShoP: About page here!!',
		'text_on_page': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore vero laudantium quaerat in odit? Sapiente, saepe! Suscipit dolores ducimus odit quae necessitatibus, neque hic cumque exercitationem, ut corrupti, minima saepe!'
	}

	return render(request, 'main/about.html', context)
