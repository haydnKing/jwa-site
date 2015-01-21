# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0009_auto_20150121_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, default='s', choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(help_text="The person's main role", max_length=1, choices=[('c', 'Graduate Student'), ('f', 'Advisor'), ('a', 'Principal Investigator'), ('b', 'Postdoctorial Researcher'), ('d', 'Undergraduate Student'), ('e', 'Collaborator')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('g', 'Prof.'), ('c', 'Mrs'), ('f', 'Dr'), ('a', 'Mr'), ('b', 'Ms'), ('d', 'Miss'), ('e', 'Mx')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='banner_image',
            field=models.ImageField(blank=True, upload_to='project_images/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')]),
            preserve_default=True,
        ),
    ]
