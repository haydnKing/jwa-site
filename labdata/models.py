from django.db import models

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

	name = models.CharField(max_length=512)
	title = models.CharField(max_length=1, choices=list(TITLE_CHOICES.items()))
	role = models.CharField(max_length=1, choices=list(ROLE_CHOICES.items()))
	bio = models.TextField(blank=True)
	mug_shot = models.ImageField(blank=True)
	email = models.EmailField()

	def getTitle(self):
		return self.TITLE_CHOICES[self.title]
	getTitle.short_description = "Title"
	def getRole(self):
		return self.ROLE_CHOICES[self.role]
	getRole.short_description = "Role"

	def __str__(self):
		return "{} {}".format(self.getTitle(), self.name)

class Project(models.Model):
	TYPE_CHOICES = {
			's': 'Synbio',
			't': 'Toxoplasma',
			'o': 'Other',
		}
	name = models.CharField(max_length=256)
	type = models.CharField(max_length=1, choices=list(TYPE_CHOICES.items()))
	short_description = models.CharField(max_length=512)
	long_description = models.TextField()
	person = models.ManyToManyField(Person)

	def getType(self):
		return self.TYPE_CHOICES[self.type]
	getType.short_description = "Type"

	def __str__(self):
		return self.name


