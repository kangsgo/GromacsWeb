# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0002_auto_20161119_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url_i',
            field=models.ImageField(null=True, blank=True, verbose_name='图片', upload_to='imgas/article/%Y'),
        ),
        migrations.AlterField(
            model_name='software',
            name='image_url_i',
            field=models.ImageField(null=True, verbose_name='图片', upload_to='imgas/software/%Y'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_url_i',
            field=models.ImageField(null=True, verbose_name='图片', upload_to='imgas/video/%Y'),
        ),
    ]
