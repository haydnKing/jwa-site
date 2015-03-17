# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0017_auto_20150211_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, help_text='This identifies where the text should be put')),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='funding',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('c', 'Graduate Student'), ('e', 'Collaborator'), ('f', 'Advisor'), ('a', 'Principal Investigator'), ('b', 'Postdoctorial Researcher'), ('d', 'Undergraduate Student')], help_text="The person's main role"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('g', 'Prof.'), ('c', 'Mrs'), ('e', 'Mx'), ('f', 'Dr'), ('a', 'Mr'), ('b', 'Ms'), ('d', 'Miss')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('s', 'Synbio'), ('t', 'Toxoplasma')]),
            preserve_default=True,
        ),
    ]
