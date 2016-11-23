# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0005_auto_20161119_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_url_i',
        ),
        migrations.AlterField(
            model_name='software',
            name='image_url_i',
            field=models.ForeignKey(null=True, blank=True, verbose_name='分类', to='gromacs.Category'),
            preserve_default=False,
        ),
    ]
