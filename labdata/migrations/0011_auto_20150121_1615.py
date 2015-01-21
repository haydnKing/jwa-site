# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0010_auto_20150121_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='abstract',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.CharField(max_length=512, default='unlisted'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, help_text="The person's main role", choices=[('c', 'Graduate Student'), ('e', 'Collaborator'), ('b', 'Postdoctorial Researcher'), ('a', 'Principal Investigator'), ('f', 'Advisor'), ('d', 'Undergraduate Student')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('c', 'Mrs'), ('e', 'Mx'), ('g', 'Prof.'), ('b', 'Ms'), ('a', 'Mr'), ('f', 'Dr'), ('d', 'Miss')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('o', 'Other'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
    ]
