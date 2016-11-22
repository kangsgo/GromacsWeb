# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gromacs', '0021_auto_20161121_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefield',
            name='user',
            field=models.ForeignKey(related_name='coursefielduser', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
