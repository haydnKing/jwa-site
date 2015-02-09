# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0013_auto_20150209_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='teaser',
            field=models.TextField(help_text='Short version of the news item', default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('a', 'Principal Investigator'), ('d', 'Undergraduate Student'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('e', 'Collaborator'), ('f', 'Advisor')], help_text="The person's main role", max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('g', 'Prof.'), ('a', 'Mr'), ('d', 'Miss'), ('b', 'Ms'), ('c', 'Mrs'), ('e', 'Mx'), ('f', 'Dr')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(choices=[('t', 'Toxoplasma'), ('o', 'Other'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
    ]
