# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gromacs', '0012_remove_software_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='softuser', verbose_name='发布人'),
        ),
    ]
