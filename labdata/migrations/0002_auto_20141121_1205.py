# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(default='o', choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')], max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='mug_shot',
            field=models.ImageField(upload_to='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('e', 'Collaborator'), ('a', 'Principal Investigator'), ('f', 'Advisor'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('d', 'Undergraduate Student')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('e', 'Mx'), ('g', 'Prof.'), ('a', 'Mr'), ('f', 'Dr'), ('b', 'Ms'), ('c', 'Mrs'), ('d', 'Miss')], max_length=1),
            preserve_default=True,
        ),
    ]
