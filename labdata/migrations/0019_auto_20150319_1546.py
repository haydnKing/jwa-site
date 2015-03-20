# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0018_auto_20150317_1342'),
    ]

    operations = [
				migrations.RenameModel('Project', 'ResearchTheme')
    ]
