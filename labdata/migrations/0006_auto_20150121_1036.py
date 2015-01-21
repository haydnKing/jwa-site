# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0005_auto_20150121_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, help_text='Short background about the person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='current',
            field=models.BooleanField(default=True, verbose_name='Current Lab Member', help_text='Is this person a current member of the lab?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, help_text='Contact email - if completed this will be publically available', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='mug_shot',
            field=models.ImageField(blank=True, help_text='Optional mug shot', upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text="The person's full name", max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('f', 'Advisor'), ('e', 'Collaborator'), ('d', 'Undergraduate Student'), ('b', 'Postdoctorial Researcher'), ('a', 'Principal Investigator'), ('c', 'Graduate Student')], help_text="The person's main role", max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('g', 'Prof.'), ('f', 'Dr'), ('e', 'Mx'), ('d', 'Miss'), ('b', 'Ms'), ('a', 'Mr'), ('c', 'Mrs')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')], max_length=1),
            preserve_default=True,
        ),
    ]
