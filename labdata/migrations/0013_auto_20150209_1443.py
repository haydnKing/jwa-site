# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0012_auto_20150129_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funding',
            options={'verbose_name_plural': 'Funding items', 'verbose_name': 'Funding item'},
        ),
        migrations.AddField(
            model_name='funding',
            name='type',
            field=models.CharField(choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')], max_length=1, default='s'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_body_logo',
            field=models.ImageField(upload_to='', verbose_name='logo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_body_name',
            field=models.CharField(verbose_name='Name', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_body_url',
            field=models.URLField(blank=True, verbose_name='URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_PIs',
            field=models.ManyToManyField(related_name='Funding_PI', verbose_name='Principal Investigator(s)', to='labdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_coinvestigators',
            field=models.ManyToManyField(related_name='Funding_CI', blank=True, verbose_name='Co-Investigators', to='labdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_description',
            field=tinymce.models.HTMLField(verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_more_info',
            field=models.URLField(blank=True, verbose_name='More Info (URL)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_title',
            field=models.CharField(verbose_name='Title', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('e', 'Collaborator'), ('d', 'Undergraduate Student'), ('a', 'Principal Investigator'), ('f', 'Advisor'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student')], max_length=1, help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('g', 'Prof.'), ('e', 'Mx'), ('d', 'Miss'), ('a', 'Mr'), ('f', 'Dr'), ('b', 'Ms'), ('c', 'Mrs')], max_length=1),
            preserve_default=True,
        ),
    ]
