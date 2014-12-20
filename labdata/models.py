from django.db import models
import urllib.parse
from tinymce import models as tinymce_models
from orderedmodel import OrderedModel

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
	ROLE_CHOICES_PL = {
		'a': 'Principal Investigator', #Should only be one of these
		'b': 'Postdoctorial Researchers',
		'c': 'Graduate Students',
		'd': 'Undergraduate Students',
		'e': 'Collaborators',
		'f': 'Advisors',
	}

	name = models.CharField(max_length=512)
	title = models.CharField(max_length=1, choices=list(TITLE_CHOICES.items()))
	role = models.CharField(max_length=1, choices=list(ROLE_CHOICES.items()))
	bio = models.TextField(blank=True)
	mug_shot = models.ImageField(blank=True)
	email = models.EmailField()
	slug = models.SlugField(unique=True)
	current = models.BooleanField(default=True, 
			verbose_name="Current Lab Member")

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
	TYPE_CHOICES = {
			's': 'Synbio',
			't': 'Toxoplasma',
			'o': 'Other',
		}
	name = models.CharField(max_length=256)
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	short_description = models.CharField(max_length=512)
	long_description = tinymce_models.HTMLField()
	person = models.ManyToManyField(Person)
	slug = models.SlugField(unique=True)

	def getType(self):
		return self.TYPE_CHOICES[self.type]
	getType.short_description = "Type"

	def area(self):
		if self.type == 's':
			return 'synbio'
		elif self.type == 't':
			return 'toxo'
		return 'other'

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
	desc = models.TextField(verbose_name="description")
	url = models.URLField()
	icon = models.ImageField(blank=True)

	def __str__(self):
		return "{} : {}".format(self.title, self.url)



