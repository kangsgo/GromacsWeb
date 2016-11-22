# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0025_auto_20161122_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='内容', null=True),
        ),
        migrations.AlterField(
            model_name='bash',
            name='content',
            field=models.TextField(blank=True, verbose_name='正文', null=True),
        ),
        migrations.AlterField(
            model_name='coursefield',
            name='content',
            field=models.TextField(blank=True, verbose_name='内容', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True, verbose_name='页面内容', null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='content',
            field=models.TextField(blank=True, verbose_name='正文', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='abstact',
            field=models.TextField(blank=True, verbose_name='简介', null=True),
        ),
    ]
