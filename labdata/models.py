from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=512)
	title = models.CharField(max_length=1, choices=(
		('a','Mr'),
		('b','Ms'),
		('c','Mrs'),
		('d','Miss'),
		('e','Mx'),
		('f','Dr'),
		('g','Prof.'),
		))
	role = models.CharField(max_length=1, choices=(
		('a','Principal Investigator'),
		('b', 'Postdoctorial Researcher'),
		('c', 'Graduate Student'),
		('d', 'Undergraduate Student'),
		('e', 'Collaborator'),
		('f', 'Advisor'),
		))
	bio = models.TextField()
	mug_shot = models.ImageField()
	email = models.EmailField()

	def __str__(self):
		return dict(self.title.choices)[self.title] + self.name

class Project(models.Model):
	name = models.CharField(max_length=256)
	short_description = models.CharField(max_length=512)
	long_description = models.TextField()
	person = models.ManyToManyField(Person)


