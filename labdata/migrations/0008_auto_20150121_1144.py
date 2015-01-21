# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0007_auto_20150121_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='research_interests',
            field=tinymce.models.HTMLField(default='<p>None given</p>'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(help_text="The person's main role", max_length=1, choices=[('a', 'Principal Investigator'), ('f', 'Advisor'), ('e', 'Collaborator'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('d', 'Undergraduate Student')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('a', 'Mr'), ('f', 'Dr'), ('g', 'Prof.'), ('e', 'Mx'), ('b', 'Ms'), ('c', 'Mrs'), ('d', 'Miss')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
    ]
