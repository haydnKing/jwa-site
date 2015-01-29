from django.contrib import admin
from labdata.models import *

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from orderedmodel import OrderedModelAdmin

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class MyAdminSite(admin.AdminSite):
	site_header = "Ajioka Lab Administration"

class PersonAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'getRole')
	prepopulated_fields = {"slug": ("name",)}
	fields = ["title", "name", "role", "current", "email", "mug_shot", 
			"research_interests", "bio", "slug"]

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'getType')
	prepopulated_fields = {"slug": ("name",)}
	fields = ['name', 'type', 'short_description','banner_image',
			'long_description','person','slug',]

class RelatedLinkAdmin(OrderedModelAdmin):
	list_display = ('text', 'url', 'reorder')

class ResourceAdmin(OrderedModelAdmin):
	list_display = ('title', 'url', 'reorder')
	fields = ['title', 'type', 'icon', 'url', 'desc',]

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')

	fields = ['type', 'title', 'authors', 'journal', 'date',
			'link', 'people', 'document',]

class FundingAdmin(admin.ModelAdmin):
	list_display = ('grant_title', 'funding_body_name')

	fieldsets = (
			('Funding Body',{
				'fields': ('funding_body_name', 'funding_body_url',
					'funding_body_logo'),
			}),
			('Grant Information', {
				'fields': ('grant_title', 'grant_PIs', 'grant_coinvestigators',
					'grant_more_info', 'grant_description')
			}),
		)

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Person, PersonAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(RelatedLink, RelatedLinkAdmin)
admin_site.register(Resource, ResourceAdmin)
admin_site.register(Publication, PublicationAdmin)
admin_site.register(Funding, FundingAdmin)

admin_site.register(FlatPage, FlatPageAdmin)

