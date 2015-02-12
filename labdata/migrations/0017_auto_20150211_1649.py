# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0016_auto_20150211_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='banner_image',
            field=models.ImageField(help_text='Should be 900px or more wide', upload_to='news_images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(help_text="The person's main role", max_length=1, choices=[('d', 'Undergraduate Student'), ('f', 'Advisor'), ('b', 'Postdoctorial Researcher'), ('a', 'Principal Investigator'), ('c', 'Graduate Student'), ('e', 'Collaborator')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('d', 'Miss'), ('f', 'Dr'), ('b', 'Ms'), ('g', 'Prof.'), ('a', 'Mr'), ('c', 'Mrs'), ('e', 'Mx')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='banner_image',
            field=models.ImageField(help_text='Should be 900px or more wide', upload_to='project_images/', blank=True),
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
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('s', 'Synbio'), ('t', 'Toxoplasma'), ('o', 'Other')]),
            preserve_default=True,
        ),
    ]
