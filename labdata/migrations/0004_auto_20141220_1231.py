# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0003_auto_20141220_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relatedlink',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='relatedlink',
            name='order',
            field=models.PositiveIntegerField(unique=True, blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='order',
            field=models.PositiveIntegerField(unique=True, blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student'), ('f', 'Advisor'), ('d', 'Undergraduate Student'), ('e', 'Collaborator'), ('a', 'Principal Investigator')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('b', 'Ms'), ('c', 'Mrs'), ('g', 'Prof.'), ('f', 'Dr'), ('d', 'Miss'), ('e', 'Mx'), ('a', 'Mr')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('t', 'Toxoplasma'), ('s', 'Synbio'), ('o', 'Other')]),
            preserve_default=True,
        ),
    ]
