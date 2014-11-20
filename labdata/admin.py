from django.contrib import admin
from labdata.models import Person, Project

class PersonAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'getRole')

admin.site.register(Person, PersonAdmin)
admin.site.register(Project)

