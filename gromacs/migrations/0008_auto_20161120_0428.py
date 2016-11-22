# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0007_article_image_url_i'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categeory',
            field=models.ForeignKey(verbose_name='分类', to='gromacs.Category'),
        ),
        migrations.AlterField(
            model_name='software',
            name='image_url_i',
            field=models.ImageField(upload_to='software/%Y', null=True, verbose_name='图片', blank=True),
        ),
    ]
