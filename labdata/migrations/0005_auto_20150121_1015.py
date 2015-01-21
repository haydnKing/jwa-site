# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0004_auto_20141220_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funding_body_name', models.CharField(max_length=128)),
                ('funding_body_url', models.URLField()),
                ('funding_body_logo', models.ImageField(upload_to='', blank=True)),
                ('grant_title', models.CharField(max_length=256)),
                ('grant_description', tinymce.models.HTMLField()),
                ('grant_date', models.DateField()),
                ('grant_more_info', models.URLField()),
                ('grant_PIs', models.ManyToManyField(related_name='Funding_PI', to='labdata.Person')),
                ('grant_coinvestigators', models.ManyToManyField(related_name='Funding_CI', to='labdata.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=512)),
                ('banner_image', models.ImageField(upload_to='', blank=True)),
                ('content', tinymce.models.HTMLField()),
                ('show_on_homepage', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('date', models.DateField()),
                ('journal', models.CharField(max_length=128)),
                ('link', models.URLField()),
                ('abstract', models.TextField()),
                ('type', models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')])),
                ('document', models.FileField(upload_to='', blank=True)),
                ('people', models.ManyToManyField(to='labdata.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('d', 'Undergraduate Student'), ('e', 'Collaborator'), ('b', 'Postdoctorial Researcher'), ('a', 'Principal Investigator'), ('f', 'Advisor'), ('c', 'Graduate Student')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('d', 'Miss'), ('e', 'Mx'), ('b', 'Ms'), ('a', 'Mr'), ('f', 'Dr'), ('g', 'Prof.'), ('c', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
    ]
