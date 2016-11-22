# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import ajaximage.fields


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
            field=ajaximage.fields.AjaxImageField(default=datetime.datetime(2016, 11, 19, 12, 1, 49, 912214, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
