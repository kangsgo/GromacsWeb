# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0022_coursefield_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_url_i',
        ),
        migrations.RemoveField(
            model_name='software',
            name='image_url_i',
        ),
        migrations.RemoveField(
            model_name='video',
            name='image_url_i',
        ),
    ]
