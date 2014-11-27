from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404

from labdata.models import Project, Person

def home(request):
	return render(request, 'home.html')

def projects(request, area):
	#get projects from database
	if area == None:
		projects = Project.objects.all()
	elif area == 'toxo':
		projects = Project.objects.filter(type='t')
	elif area == 'synbio':
		projects = Project.objects.filter(type='s')

	return render(request, 'projects.html', {
		'projects': projects.order_by('name'),
		'area': area,
	})

def project(request, slug):
	"""Project detail page"""
	project = get_object_or_404(Project, slug=slug)
	ctx = {
				'title': 'Ajioka Lab',
				'project': project,
				'projects': Project.objects.filter(type=project.type).order_by('name'),
				'area': None,
	}
	if project.type == 't':
		ctx['area'] = 'toxo'
	elif project.type == 's':
		ctx['area'] = 'synbio'

	return render(request, 'project.html', ctx)


def people(request):
	ctx = {
				'people': Person.objects.all().order_by('name'),
	}
	return render(request, 'people.html', ctx)

def person(request, slug):
	person = get_object_or_404(Person, slug=slug)
	return render(request, 'person.html', {
		'person': person,
		'people': Person.objects.all().order_by('name')
		})

def publications(request):
	return render(request, 'publications.html', {})

contexts = {
	'news': {
				'title': 'Ajioka Lab',
				'subtitle': 'News',
				'breadcrumbs': [ ['/', 'Ajioka Lab',],
												 ['/news', 'News']],
				'vbreadcrumbs': [ ['/news', 'News'],],
				'localnav': [],
	},
	'resources': {
				'title': 'Ajioka Lab',
				'subtitle': 'Resources',
				'breadcrumbs': [ ['/', 'Ajioka Lab',],
												 ['/resources', 'Resources']],
				'vbreadcrumbs': [ ['/resources', 'Resources'],],
				'localnav': [['/resources/synbio', 'Synthetic Biology',],
										 ['/resources/toxo', 'Toxoplasma Gondii',],
					],
	},
	'funding': {
				'title': 'Ajioka Lab',
				'subtitle': 'Funding',
				'breadcrumbs': [ ['/', 'Ajioka Lab',],
												 ['/funding', 'Funding']],
				'vbreadcrumbs': [ ['/funding', 'Funding'],],
				'localnav': [['/funding/grant1', 'Grant 1',],
										 ['/funding/grant2', 'Grant 2',],
										 ['/funding/grantN', 'Grant N',],
					],
	},
	'about': {
				'title': 'Ajioka Lab',
				'subtitle': 'About',
				'breadcrumbs': [ ['/', 'Ajioka Lab',],
												 ['/about', 'About']],
				'vbreadcrumbs': [ ['/about', 'About'],],
				'localnav': [['/about/synbio', 'Synthetic Biology',],
										 ['/about/toxo', 'Toxoplasma Gondii',],
										 ['/about/contact', 'Contact',],
					],
	},
	'publications': {
				'title': 'Ajioka Lab',
				'subtitle': 'Publications',
				'breadcrumbs': [ ['/', 'Ajioka Lab',],
												 ['/publications', 'Publications']],
				'vbreadcrumbs': [ ['/publications', 'Publications'],],
				'localnav': [['/publications/synbio', 'Synthetic Biology',],
										 ['/publications/toxo', 'Toxoplasma Gondii',],
					],
	},
}

def subsection(request, name):
	try:
		return render(request, 'sub-section.html', contexts[name])
	except KeyError:
		raise Http404
