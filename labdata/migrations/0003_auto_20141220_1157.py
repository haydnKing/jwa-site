# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0002_auto_20141209_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.CharField(max_length=128)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('desc', models.TextField(verbose_name='description')),
                ('url', models.URLField()),
                ('icon', models.ImageField(blank=True, upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='current',
            field=models.BooleanField(default=True, verbose_name='Current Lab Member'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=1, choices=[('f', 'Advisor'), ('d', 'Undergraduate Student'), ('e', 'Collaborator'), ('a', 'Principal Investigator'), ('b', 'Postdoctorial Researcher'), ('c', 'Graduate Student')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=1, choices=[('f', 'Dr'), ('d', 'Miss'), ('e', 'Mx'), ('a', 'Mr'), ('g', 'Prof.'), ('b', 'Ms'), ('c', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=1, choices=[('o', 'Other'), ('t', 'Toxoplasma'), ('s', 'Synbio')]),
            preserve_default=True,
        ),
    ]
