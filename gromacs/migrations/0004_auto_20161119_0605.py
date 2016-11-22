# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0003_auto_20161119_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url_i',
            field=models.ImageField(upload_to='article/%Y', null=True, blank=True, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='software',
            name='image_url_i',
            field=models.ImageField(upload_to='software/%Y', null=True, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_url_i',
            field=models.ImageField(upload_to='video/%Y', null=True, verbose_name='图片'),
        ),
    ]
