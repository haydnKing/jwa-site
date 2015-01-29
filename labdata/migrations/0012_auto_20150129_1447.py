# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0011_auto_20150121_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='grant_date',
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_body_logo',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='funding_body_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funding',
            name='grant_more_info',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('b', 'Postdoctorial Researcher'), ('f', 'Advisor'), ('d', 'Undergraduate Student'), ('a', 'Principal Investigator'), ('e', 'Collaborator'), ('c', 'Graduate Student')], help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('b', 'Ms'), ('f', 'Dr'), ('d', 'Miss'), ('g', 'Prof.'), ('a', 'Mr'), ('e', 'Mx'), ('c', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(max_length=512, help_text='All authors listed on the paper (used for citations)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='people',
            field=models.ManyToManyField(to='labdata.Person', help_text='Lab contibutors (a citation will appear on\ttheir page).'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')]),
            preserve_default=True,
        ),
    ]
