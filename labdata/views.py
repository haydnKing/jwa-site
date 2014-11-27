from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404

from labdata.models import Project, Person

def home(request):
	return render(request, 'home.html')

def projects(request, area):
	print("Projects")
	if area == None:
		projects = Project.objects.all()
	elif area == 'toxo':
		projects = Project.objects.filter(type='t')
	elif area == 'synbio':
		projects = Project.objects.filter(type='s')
	elif area == 'other':
		projects = Project.objects.filter(type='o')

	return render(request, 'projects.html', {
		'projects': projects.order_by('name'),
		'area': area,
		'show_links': True,
		'subtitle': 'projects',
	})

def project(request, area, slug):
	"""Project detail page"""
	print("Project")
	if area == 'toxo':
		a='t'
	elif area == 'synbio':
		a='s'
	elif area == 'other':
		a='o'

	project = get_object_or_404(Project, slug=slug, type=a)
	ctx = {
				'title': 'Ajioka Lab',
				'subtitle': 'projects',
				'project': project,
				'projects': Project.objects.filter(type=project.type).order_by('name'),
				'area': area,
				'show_links': False,
	}

	return render(request, 'project.html', ctx)

def people(request):
	people = Person.objects.all().order_by('name')
	roles = ['a','b','c','d','e','f',]
	people_by_role = [(Person.ROLE_CHOICES_PL[r], people.filter(role=r)) for r in roles]
	return render(request, 'people.html', {
		'people': people,
		'show_links': True,
		'people_by_role': people_by_role,
	})

def person(request, slug):
	people = Person.objects.all().order_by('name')
	person = people.get(slug=slug)
	
	return render(request, 'person.html', {
		'people': people,
		'show_links': False,
		'person': person,
	})
