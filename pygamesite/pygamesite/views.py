from django.shortcuts import render

# simple: are they logged in or not?
def landingPage(request):
	"""Main landing page"""
	return(render(request, 'index.html', {'username':'Monty'}))

