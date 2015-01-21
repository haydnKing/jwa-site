# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0008_auto_20150121_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='banner_image',
            field=models.ImageField(upload_to='', blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('d', 'Undergraduate Student'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('e', 'Collaborator'), ('a', 'Principal Investigator'), ('f', 'Advisor')], help_text="The person's main role", max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('g', 'Prof.'), ('d', 'Miss'), ('b', 'Ms'), ('c', 'Mrs'), ('e', 'Mx'), ('a', 'Mr'), ('f', 'Dr')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
    ]
