# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0011_software_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='user',
        ),
    ]
