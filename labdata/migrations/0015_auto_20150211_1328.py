# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0014_auto_20150209_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('b', 'Postdoctorial Researcher'), ('e', 'Collaborator'), ('c', 'Graduate Student'), ('a', 'Principal Investigator'), ('d', 'Undergraduate Student'), ('f', 'Advisor')], help_text="The person's main role", max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('b', 'Ms'), ('e', 'Mx'), ('c', 'Mrs'), ('g', 'Prof.'), ('a', 'Mr'), ('d', 'Miss'), ('f', 'Dr')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')], max_length=1),
            preserve_default=True,
        ),
    ]
