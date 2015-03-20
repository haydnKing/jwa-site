# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0019_auto_20150319_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'Content'},
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=32, unique=True, help_text='This identifies where the text should be put'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('a', 'Principal Investigator'), ('d', 'Undergraduate Student'), ('f', 'Advisor'), ('e', 'Collaborator'), ('c', 'Graduate Student'), ('b', 'Postdoctorial Researcher')], help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('a', 'Mr'), ('d', 'Miss'), ('f', 'Dr'), ('e', 'Mx'), ('g', 'Prof.'), ('c', 'Mrs'), ('b', 'Ms')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researchtheme',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
    ]
