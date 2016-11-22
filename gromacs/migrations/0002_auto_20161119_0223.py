# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='reference',
            field=models.ForeignKey(to='gromacs.ReferenceLink', blank=True, verbose_name='参考链接', null=True),
        ),
    ]
