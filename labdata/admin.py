from django.contrib import admin
from labdata.models import Person, Project

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

class MyAdminSite(admin.AdminSite):
	site_header = "Ajioka Lab Administration"

class PersonAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'getRole')
	prepopulated_fields = {"slug": ("name",)}

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'getType')
	prepopulated_fields = {"slug": ("name",)}

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Person, PersonAdmin)
admin_site.register(Project, ProjectAdmin)

