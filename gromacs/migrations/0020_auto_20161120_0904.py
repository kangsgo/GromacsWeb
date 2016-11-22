# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gromacs', '0019_software_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(related_name='bloguser', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bash',
            name='user',
            field=models.ForeignKey(related_name='bashuser', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(related_name='courseuser', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(related_name='videouser', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
