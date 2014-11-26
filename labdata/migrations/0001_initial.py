# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('title', models.CharField(max_length=1, choices=[('a', 'Mr'), ('f', 'Dr'), ('c', 'Mrs'), ('g', 'Prof.'), ('b', 'Ms'), ('e', 'Mx'), ('d', 'Miss')])),
                ('role', models.CharField(max_length=1, choices=[('a', 'Principal Investigator'), ('f', 'Advisor'), ('c', 'Graduate Student'), ('b', 'Postdoctorial Researcher'), ('e', 'Collaborator'), ('d', 'Undergraduate Student')])),
                ('bio', models.TextField(blank=True)),
                ('mug_shot', models.ImageField(upload_to='', blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')])),
                ('short_description', models.CharField(max_length=512)),
                ('long_description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('person', models.ManyToManyField(to='labdata.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
