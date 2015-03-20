from django.shortcuts import get_object_or_404
import django.shortcuts
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import datetime, random
from itertools import chain
from labdata.models import *

def render(request, template, context):
	context['related_links'] = RelatedLink.objects.all().order_by('order')
	return django.shortcuts.render(request, template, context)
	
def get_content(name):
	try:
		o = Content.objects.get(name=name)
	except ObjectDoesNotExist:
		return "<p>No content found for '{}'</p>".format(name)
	return o.content

def home(request):
	news = NewsItem.objects.filter(show_on_homepage=True).order_by('-pub_date')[:3]
	carosel = list(chain(
			NewsItem.objects.filter(show_on_homepage=True,
				pub_date__gte = datetime.datetime.now() - datetime.timedelta(days=60)),
			ResearchTheme.objects.all()))

	#choose 3
	carosel = random.sample(carosel, 3)

	return render(request, 'home.html', {
		'greeting': get_content('home_greeting'),
		'toxo': get_content('home_toxo'),
		'synbio': get_content('home_synbio'),
		'news': news,
		'carosel': carosel,
	})

# --------------------- LISTING PAGES -----------
SB = 'Synthetic Biology'
SBi = 'synbio'
TX = 'Toxoplasma Gondii'
TXi = 'toxo'
OT = 'Other'
OTi = 'other'
def research_themes(request):
	return render(request, 'researchthemes.html', {
		'themes': ResearchTheme.objects.all().order_by('name'),
		'show_links': False,
		'subtitle': 'Research Themes',
		'name': 'research_themes',
		'listing_template': 'researchtheme_listing.html',
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
		'name': 'resources',
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
		'name': 'funding',
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
		'name': 'publications',
		'listing_template': 'publication_listing.html',
		})

def news(request):
	obj = NewsItem.objects.all().order_by('-pub_date')[:6]
	localnav = [(o.title, reverse('labdata:news_item', kwargs = { 
		'year':  o.pub_date.year, 
		'month': o.pub_date.month, 
		'day':   o.pub_date.day, 
		'slug':  o.slug})) for o in obj]
	localnav.append(("News Archive", reverse('labdata:news_archive'),))
	return render(request, 'listing.html', {
		'items': [
			{
				'title': "Latest News",
				'id': None,
				'objects': obj,
			},
		],
		'localnav': localnav,
		'subtitle': 'News',
		'name': 'news',
		'listing_template': 'news_listing.html',
		})

def news_archive(request):
	years = [y.year for y in NewsItem.objects.dates('pub_date', 'year')]
	years = sorted(years, reverse=True)
	items = [{
		'title': str(year),
		'id': 'year_{}'.format(year),
		'objects':
		NewsItem.objects.filter(pub_date__year=year).order_by('-pub_date'),
		} for year in years]

	
	return render(request, 'listing.html', {
		'items': items,
		'subtitle': 'News Archive',
		'name': 'news_archive',
		'extracrumbs': [('News', reverse('labdata:news'),)],
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
		'name': 'people',
		'listing_template': 'people_listing.html',
	})

#-------------- SINGLE PAGES
def research_theme(request, slug):
	"""research theme detail page"""

	theme = get_object_or_404(ResearchTheme, slug=slug)
	ctx = {
				'title': 'Ajioka Lab',
				'subtitle': 'research_theme',
				'theme': theme,
				'themes': ResearchTheme.objects.all().order_by('name'),
				'show_links': False,
	}

	return render(request, 'research_theme.html', ctx)

def person(request, slug):
	people = Person.objects.all().order_by('name')
	person = people.get(slug=slug)
	
	return render(request, 'person.html', {
		'people': people,
		'show_links': False,
		'person': person,
		'themes': person.researchtheme_set.all(),
		'publications': person.publication_set.all(),
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

def about(request):
	return render(request, 'about.html', {
		'about': get_content('about'),
		'about_synbio': get_content('about_synbio'),
		'about_toxo': get_content('about_toxo'),
		})
