from django.db import models
import urllib.parse, datetime
from tinymce import models as tinymce_models
from orderedmodel import OrderedModel
from django.core.urlresolvers import reverse

TYPE_CHOICES = {
		's': 'Synbio',
		't': 'Toxoplasma',
		'o': 'Other',
}
LONG_TYPES = {
		's': 'Synthetic Biology',
		't': 'Toxoplasma Gondii',
		'o': 'Other',
}


class Person(models.Model):
	class Meta:
		verbose_name_plural = 'People'

	TITLE_CHOICES = {
		'a':'Mr',
		'b':'Ms',
		'c':'Mrs',
		'd':'Miss',
		'e':'Mx',
		'f':'Dr',
		'g':'Prof.',
	}
	ROLE_CHOICES = {
		'a': 'Principal Investigator',
		'b': 'Postdoctorial Researcher',
		'c': 'Graduate Student',
		'd': 'Undergraduate Student',
		'e': 'Collaborator',
		'f': 'Advisor',
	}

	name = models.CharField(max_length=512, 
			help_text="The person's full name")
	title = models.CharField(max_length=1, 
			choices=list(TITLE_CHOICES.items()))
	role = models.CharField(max_length=1, 
			choices=list(ROLE_CHOICES.items()),
			help_text="The person's main role")
	bio = models.TextField(blank=True,
			help_text="Short background about the person")
	research_interests = tinymce_models.HTMLField()
	mug_shot = models.ImageField(blank=True, upload_to="mugshots/",
			help_text="Optional mug shot")
	email = models.EmailField(blank=True,
			help_text="Contact email - if completed this will be publically available")
	slug = models.SlugField(unique=True, 
		help_text="This text must uniquely identify the person in the database")
	current = models.BooleanField(default=True, 
			verbose_name="Current Lab Member",
			help_text="Is this person a current member of the lab?")

	def getTitle(self):
		return self.TITLE_CHOICES[self.title]
	getTitle.short_description = "Title"
	def getRole(self):
		return self.ROLE_CHOICES[self.role]
	getRole.short_description = "Role"
	def fullName(self):
		return "{} {}".format(self.getTitle(), self.name)
	fullName.short_description = "fullName"


	def __str__(self):
		return self.fullName();

DEFAULT_THEME_BANNER = 'images/content/carousel-4.png'
DEFAULT_THEME_TEASER = 'images/content/image-placeholder.jpg'
class ResearchTheme(models.Model):
	name = models.CharField(max_length=256)
	short_description = models.TextField()
	teaser_image = models.ImageField(blank=True, upload_to="project_images/",
			help_text='Small image to show in \"Research Themes\" page, 100x100px')
	long_description = tinymce_models.HTMLField()
	person = models.ManyToManyField(Person)
	slug = models.SlugField(unique=True)
	banner_image = models.ImageField(blank=True, upload_to="project_images/",
			help_text='To be shown above the theme page and in the carosel on the homepage, 900x400px')

	def get_banner_url(self):
		if self.banner_image:
			return self.banner_image.url
		return DEFAULT_THEME_BANNER

	def get_teaser_url(self):
		if self.teaser_image:
			return self.teaser_image.url
		return DEFAULT_THEME_TEASER

	def get_url(self):
		return reverse('labdata:research_theme', kwargs={'slug':self.slug})

	def __str__(self):
		return self.name

class RelatedLink(OrderedModel):
	"""Related links for the sidebar"""
	text = models.CharField(max_length=128)
	url = models.URLField()

	def __str__(self):
		return "{} : {}".format(self.text, self.url)

class Resource(OrderedModel):
	"""A list of useful resources - more complete than the related links"""
	title = models.CharField(max_length=64)
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	desc = models.TextField(verbose_name="description")
	url = models.URLField()
	icon = models.ImageField(blank=True)

	def __str__(self):
		return "{} : {}".format(self.title, self.url)


class Publication(models.Model):
	"""Lab publications"""
	title = models.CharField(max_length=512)
	authors = models.CharField(max_length=512, 
		help_text="All authors listed on the paper (used for citations)")
	date = models.DateField()
	journal = models.CharField(max_length=128)
	link = models.URLField()

	people = models.ManyToManyField(Person, 
			help_text="Lab contibutors (a citation will appear on	their page).")
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	document = models.FileField(blank=True)

class Funding(models.Model):
	"""Lab funding"""
	#Funding body
	funding_body_name = models.CharField(max_length=128,
			verbose_name='Name')
	funding_body_url = models.URLField(blank=True,
			verbose_name='URL')
	funding_body_logo = models.ImageField(
			verbose_name='logo')

	#Grant info
	grant_title = models.CharField(max_length=256,
			verbose_name='Title')
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	grant_PIs = models.ManyToManyField(Person, related_name="Funding_PI",
			verbose_name='Principal Investigator(s)')
	grant_coinvestigators = models.ManyToManyField(Person, 
		related_name="Funding_CI",
		verbose_name="Co-Investigators",
		blank=True)
	grant_description = tinymce_models.HTMLField(
			verbose_name="Description")
	grant_more_info = models.URLField(blank=True,
			verbose_name="More Info (URL)")

	class Meta:
		verbose_name_plural = 'Funding items'
		verbose_name = 'Funding item'

DEFAULT_NEWSITEM_BANNER = 'images/content/carousel-4.png'
class NewsItem(models.Model):
	"""News from the lab"""
	pub_date = models.DateField(default=datetime.date.today)
	title = models.CharField(max_length=512)
	banner_image = models.ImageField(blank=True, upload_to="news_images/", 
			help_text='Should be 900px or more wide')
	teaser = models.TextField(help_text="Short version of the news item")
	content = tinymce_models.HTMLField()
	show_on_homepage = models.BooleanField(default=True)

	slug = models.SlugField(unique=True)

	def get_banner_url(self):
		if self.banner_image:
			return self.banner_image.url
		return DEFAULT_NEWSITEM_BANNER

	def get_url(self):
		pd = self.pub_date
		return reverse('labdata:news_item', kwargs={
			'year':pd.year, 
			'month': pd.month, 
			'day': pd.day, 
			'slug': self.slug,
			})

	def published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(months=2)
	published_recently.admin_order_field = 'pub_date'
	published_recently.boolean = True
	published_recently.short_description = 'Published recently?'

class Content(models.Model):
	"""Text content which we might want to update every now and again"""
	class Meta:
		verbose_name_plural = 'Content'

	name = models.CharField(max_length=32, unique=True,
			help_text="This identifies where the text should be put")
	content = tinymce_models.HTMLField()
