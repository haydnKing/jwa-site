# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('f', 'Advisor'), ('a', 'Principal Investigator'), ('d', 'Undergraduate Student'), ('b', 'Postdoctorial Researcher'), ('e', 'Collaborator'), ('c', 'Graduate Student')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('f', 'Dr'), ('a', 'Mr'), ('d', 'Miss'), ('g', 'Prof.'), ('b', 'Ms'), ('e', 'Mx'), ('c', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
    ]
