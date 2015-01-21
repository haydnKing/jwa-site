# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0006_auto_20150121_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mug_shot',
            field=models.ImageField(blank=True, help_text='Optional mug shot', upload_to='mugshots/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('d', 'Undergraduate Student'), ('a', 'Principal Investigator'), ('e', 'Collaborator'), ('f', 'Advisor')], help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(unique=True, help_text='This text must uniquely identify the person in the database'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('b', 'Ms'), ('c', 'Mrs'), ('d', 'Miss'), ('g', 'Prof.'), ('a', 'Mr'), ('e', 'Mx'), ('f', 'Dr')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
    ]
