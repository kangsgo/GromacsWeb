# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0026_auto_20161122_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='bash',
            name='short_text',
            field=models.ForeignKey(null=True, blank=True, verbose_name='分类', to='gromacs.Category'),
            preserve_default=False,
        ),
    ]
