# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0004_auto_20161119_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categeory',
            field=models.ForeignKey(null=True, blank=True, verbose_name='分类', to='gromacs.Category'),
        ),
    ]
