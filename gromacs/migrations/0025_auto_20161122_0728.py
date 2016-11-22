# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0024_auto_20161122_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bash',
            name='content',
            field=models.TextField(blank=True, verbose_name='内容', null=True),
        ),
    ]
