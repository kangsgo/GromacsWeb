# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0028_auto_20161122_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bash',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, blank=True, verbose_name='正文'),
        ),
    ]
