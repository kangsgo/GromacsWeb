# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gromacs', '0020_auto_20161120_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tags', models.CharField(verbose_name='标签', max_length=50)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('content', models.TextField(verbose_name='内容', null=True, blank=True)),
            ],
            options={
                'verbose_name': '教程小段',
                'ordering': ['-date_time'],
                'verbose_name_plural': '教程小段',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.AddField(
            model_name='coursefield',
            name='course',
            field=models.ForeignKey(to='gromacs.Course'),
        ),
    ]
