from django.shortcuts import get_object_or_404
import django.shortcuts
from django.http import Http404

from django.contrib.flatpages.models import FlatPage

from labdata.models import Project, Person, RelatedLink, Resource, Publication

def render(request, template, context):
	context['related_links'] = RelatedLink.objects.all().order_by('order')
	return django.shortcuts.render(request, template, context)
	

def home(request):
	fp = get_object_or_404(FlatPage, title="Home")
	return render(request, 'home.html', {'flatpage': fp})

def projects(request):
	return render(request, 'listing.html', {
		'synbio': Project.objects.filter(type='s').order_by('name'),
		'toxo':   Project.objects.filter(type='t').order_by('name'),
		'other':  Project.objects.filter(type='o').order_by('name'),
		'show_links': True,
		'subtitle': 'projects',
		'listing_template': 'project_listing.html',
	})

def project(request, slug):
	"""Project detail page"""

	project = get_object_or_404(Project, slug=slug)
	ctx = {
				'title': 'Ajioka Lab',
				'subtitle': 'projects',
				'project': project,
				'projects': Project.objects.filter(type=project.type).order_by('name'),
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
		'projects': person.project_set.all(),
		'publications': person.publication_set.all(),
	})

def resources(request):
	return render(request, 'listing.html', {
		'synbio': Resource.objects.filter(type='s'),
		'toxo':   Resource.objects.filter(type='t'),
		'other':  Resource.objects.filter(type='o'),
		'subtitle': 'resources',
		'listing_template': 'resource_listing.html',
		})

def publications(request):
	return render(request, 'listing.html', {
		'synbio': Publication.objects.filter(type='s'),
		'toxo':   Publication.objects.filter(type='t'),
		'other':  Publication.objects.filter(type='o'),
		'subtitle': 'publications',
		'listing_template': 'publication_listing.html',
		})
