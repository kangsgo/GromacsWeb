# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0006_auto_20161119_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url_i',
            field=models.ImageField(upload_to='article/%Y', verbose_name='图片', blank=True, null=True),
        ),
    ]
