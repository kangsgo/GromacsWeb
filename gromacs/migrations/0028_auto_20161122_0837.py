# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0027_bash_short_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bash',
            name='short_text',
        ),
        migrations.AddField(
            model_name='article',
            name='image_url_i',
            field=models.ImageField(verbose_name='图片', upload_to='article/%Y', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='image_url_i',
            field=models.ImageField(verbose_name='图片', upload_to='video/%Y', null=True),
        ),
    ]
