# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0026_auto_20161122_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='bash',
            name='short_text',
            field=redactor.fields.RedactorField(verbose_name='Text', default=1),
            preserve_default=False,
        ),
    ]
