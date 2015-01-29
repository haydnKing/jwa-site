from django.db import models
import urllib.parse
from tinymce import models as tinymce_models
from orderedmodel import OrderedModel

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

class Project(models.Model):
	name = models.CharField(max_length=256)
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	short_description = models.CharField(max_length=512)
	long_description = tinymce_models.HTMLField()
	person = models.ManyToManyField(Person)
	slug = models.SlugField(unique=True)
	banner_image = models.ImageField(blank=True, upload_to="project_images/")

	def getType(self):
		return TYPE_CHOICES[self.type]
	getType.short_description = "Type"

	def area(self):
		if self.type == 's':
			return 'synbio'
		elif self.type == 't':
			return 'toxo'
		return 'other'

	def longArea(self):
		return LONG_TYPES[self.type]

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
	grant_PIs = models.ManyToManyField(Person, related_name="Funding_PI",
			verbose_name='Principal Investigator(s)')
	grant_coinvestigators = models.ManyToManyField(Person, 
		related_name="Funding_CI",
		verbose_name="Co-Investigators")
	grant_description = tinymce_models.HTMLField(
			verbose_name="Description")
	grant_more_info = models.URLField(blank=True,
			verbose_name="More Info (URL)")

	class Meta:
		verbose_name_plural = 'Funding items'
		verbose_name = 'Funding item'

class NewsItem(models.Model):
	"""News from the lab"""
	pub_date = models.DateField()
	title = models.CharField(max_length=512)
	banner_image = models.ImageField(blank=True)
	content = tinymce_models.HTMLField()
	show_on_homepage = models.BooleanField(default=True)

	slug = models.SlugField(unique=True)


