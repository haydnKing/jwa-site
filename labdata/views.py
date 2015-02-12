from django.shortcuts import get_object_or_404
import django.shortcuts
from django.http import Http404
from django.core.urlresolvers import reverse

from django.contrib.flatpages.models import FlatPage

from labdata.models import *

def render(request, template, context):
	context['related_links'] = RelatedLink.objects.all().order_by('order')
	return django.shortcuts.render(request, template, context)
	

def home(request):
	fp = get_object_or_404(FlatPage, title="Home")
	return render(request, 'home.html', {'flatpage': fp})

# --------------------- LISTING PAGES -----------
SB = 'Synthetic Biology'
SBi = 'synbio'
TX = 'Toxoplasma Gondii'
TXi = 'toxo'
OT = 'Other'
OTi = 'other'
def projects(request):
	return render(request, 'listing.html', {
		'items': [
			{
				'title': SB,
				'id': SBi,
				'objects': Project.objects.filter(type='s').order_by('name'),
			},{
				'title': TX,
				'id': TXi,
				'objects': Project.objects.filter(type='t').order_by('name'),
			},{
				'title': OT,
				'id': OTi,
				'objects': Project.objects.filter(type='o').order_by('name'),
			},
		],
		'show_links': True,
		'subtitle': 'projects',
		'listing_template': 'project_listing.html',
	})

def resources(request):
	return render(request, 'listing.html', {
		'items': [
			{
				'title': SB,
				'id': SBi,
				'objects': Resource.objects.filter(type='s'),
			},{
				'title': TX,
				'id': TXi,
				'objects': Resource.objects.filter(type='t'),
			},{
				'title': OT,
				'id': OTi,
				'objects': Resource.objects.filter(type='o'),
			},
		],
		'subtitle': 'resources',
		'listing_template': 'resource_listing.html',
		})


def funding(request):
	return render(request, 'listing.html', {
		'items': [
			{
				'title': SB,
				'id': SBi,
				'objects': Funding.objects.filter(type='s'),
			},{
				'title': TX,
				'id': TXi,
				'objects': Funding.objects.filter(type='t'),
			},{
				'title': OT,
				'id': OTi,
				'objects': Funding.objects.filter(type='o'),
			},
		],
		'subtitle': 'funding',
		'listing_template': 'funding_listing.html',
		})


def publications(request):
	return render(request, 'listing.html', {
		'items': [
			{
				'title': SB,
				'id': SBi,
				'objects': Publication.objects.filter(type='s'),
			},{
				'title': TX,
				'id': TXi,
				'objects': Publication.objects.filter(type='t'),
			},{
				'title': OT,
				'id': OTi,
				'objects': Publication.objects.filter(type='o'),
			},
		],
		'subtitle': 'publications',
		'listing_template': 'publication_listing.html',
		})

def news(request):
	obj = NewsItem.objects.all().order_by('-pub_date')[:6]
	localnav = [(o.title, reverse('labdata:news_item', kwargs = { 
		'year':  o.pub_date.year, 
		'month': o.pub_date.month, 
		'day':   o.pub_date.day, 
		'slug':  o.slug})) for o in obj]
	localnav.append(("News Archive", "",))
	return render(request, 'listing.html', {
		'items': [
			{
				'title': "Latest News",
				'id': None,
				'objects': obj,
			},
		],
		'localnav': localnav,
		'subtitle': 'news',
		'listing_template': 'news_listing.html',
		})

ROLE_CHOICES_PL = (
	('a', 'Principal Investigator', 'PI'), #Should only be one of these
	('b', 'Postdoctorial Researchers', 'postdocs'),
	('c', 'Graduate Students', 'grads'),
	('d', 'Undergraduate Students', 'undergrads'),
	('e', 'Collaborators', 'collaborators'),
	('f', 'Advisors', 'advisors'),
)
def people(request):
	people = Person.objects.all().order_by('name')
	items = [{
		'title': title,
		'id': id_,
		'objects': people.filter(role=r),
	} for r,title,id_ in ROLE_CHOICES_PL]

	return render(request, 'listing.html', {
		'items': items,
		'subtitle': 'people',
		'listing_template': 'people_listing.html',
	})

#-------------- SINGLE PAGES
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

def funding_item(request, id):
	project = get_object_or_404(Funding, id=id)
	
	return render(request, 'funding_item.html', {
		'funding_item': funding_item,
		'show_links': False,
	})

def news_item(request, year, month, day, slug):
	year = int(year)
	month = int(month)
	day = int(day)
	date = datetime.date(year, month,day)

	item = get_object_or_404(NewsItem, pub_date=date, slug=slug)

	return render(request, 'news_item.html', {
		'item': item,
		'recent_items': NewsItem.objects.all().order_by('-pub_date')[:6],
	})
