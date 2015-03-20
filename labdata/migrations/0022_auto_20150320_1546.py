# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0021_auto_20150320_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('c', 'Graduate Student'), ('f', 'Advisor'), ('a', 'Principal Investigator'), ('b', 'Postdoctorial Researcher'), ('e', 'Collaborator'), ('d', 'Undergraduate Student')], help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('c', 'Mrs'), ('f', 'Dr'), ('a', 'Mr'), ('b', 'Ms'), ('g', 'Prof.'), ('e', 'Mx'), ('d', 'Miss')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researchtheme',
            name='short_description',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
    ]
