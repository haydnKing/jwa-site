# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0020_auto_20150319_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchtheme',
            name='type',
        ),
        migrations.AddField(
            model_name='researchtheme',
            name='teaser_image',
            field=models.ImageField(upload_to='project_images/', default='', help_text='Small image to show in "Research Themes" page, 100x100px', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('a', 'Principal Investigator'), ('e', 'Collaborator'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('d', 'Undergraduate Student'), ('f', 'Advisor')], max_length=1, help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('g', 'Prof.'), ('a', 'Mr'), ('e', 'Mx'), ('b', 'Ms'), ('c', 'Mrs'), ('d', 'Miss'), ('f', 'Dr')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researchtheme',
            name='banner_image',
            field=models.ImageField(upload_to='project_images/', help_text='To be shown above the theme page and in the carosel on the homepage, 900x400px', blank=True),
            preserve_default=True,
        ),
    ]
