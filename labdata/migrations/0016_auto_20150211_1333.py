# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0015_auto_20150211_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(help_text="The person's main role", choices=[('e', 'Collaborator'), ('a', 'Principal Investigator'), ('d', 'Undergraduate Student'), ('c', 'Graduate Student'), ('b', 'Postdoctorial Researcher'), ('f', 'Advisor')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('e', 'Mx'), ('a', 'Mr'), ('g', 'Prof.'), ('d', 'Miss'), ('c', 'Mrs'), ('b', 'Ms'), ('f', 'Dr')], max_length=1),
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
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')], max_length=1),
            preserve_default=True,
        ),
    ]
