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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('title', models.CharField(max_length=1, choices=[('a', 'Mr'), ('b', 'Ms'), ('c', 'Mrs'), ('d', 'Miss'), ('e', 'Mx'), ('f', 'Dr'), ('g', 'Prof.')])),
                ('role', models.CharField(max_length=1, choices=[('a', 'Principal Investigator'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('d', 'Undergraduate Student'), ('e', 'Collaborator'), ('f', 'Advisor')])),
                ('bio', models.TextField()),
                ('mug_shot', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_description', models.CharField(max_length=512)),
                ('long_description', models.TextField()),
                ('person', models.ManyToManyField(to='labdata.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
