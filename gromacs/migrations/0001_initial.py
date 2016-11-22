# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='博客标题', max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('image_url_i', models.ImageField(verbose_name='图片', upload_to='video/%Y', blank=True, null=True)),
                ('content', models.TextField(verbose_name='内容', blank=True, null=True)),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Bash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('content', models.TextField(verbose_name='正文', blank=True, null=True)),
            ],
            options={
                'verbose_name': '脚本',
                'verbose_name_plural': '脚本',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='分类名称', max_length=50)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='教程', max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('content', models.TextField(verbose_name='内容', blank=True, null=True)),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='页面标题', max_length=50)),
                ('order', models.IntegerField(verbose_name='页面顺序', default=1)),
                ('content', models.TextField(verbose_name='页面内容', blank=True, null=True)),
            ],
            options={
                'verbose_name': '页面',
                'verbose_name_plural': '页面',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ReferenceLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('url', models.URLField(verbose_name='链接', blank=True, null=True)),
            ],
            options={
                'verbose_name': '参考链接',
                'verbose_name_plural': '参考链接',
            },
        ),
        migrations.CreateModel(
            name='SoftWare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('url', models.URLField(verbose_name='链接', blank=True, null=True)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('image_url_i', models.ImageField(verbose_name='图片', upload_to='software/%Y', null=True)),
                ('content', models.TextField(verbose_name='正文', blank=True, null=True)),
                ('categeory', models.ForeignKey(to='gromacs.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '软件',
                'verbose_name_plural': '软件',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='视频题目', max_length=100)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('image_url_i', models.ImageField(verbose_name='图片', upload_to='video/%Y', null=True)),
                ('abstact', models.TextField(verbose_name='简介', blank=True, null=True)),
                ('software', models.ForeignKey(to='gromacs.SoftWare', verbose_name='软件')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='网站标题', max_length=50)),
                ('date_time', models.DateTimeField(verbose_name='日期', auto_now_add=True)),
                ('url', models.URLField(verbose_name='链接', blank=True, null=True)),
                ('content', models.CharField(verbose_name='简介', max_length=200)),
                ('linkategeory', models.ForeignKey(to='gromacs.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '网站链接',
                'verbose_name_plural': '网站链接',
                'ordering': ['-date_time'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='software',
            field=models.ForeignKey(to='gromacs.SoftWare', verbose_name='软件'),
        ),
        migrations.AddField(
            model_name='bash',
            name='categeory',
            field=models.ForeignKey(to='gromacs.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='categeory',
            field=models.ForeignKey(to='gromacs.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='reference',
            field=models.ForeignKey(blank=True, to='gromacs.ReferenceLink', verbose_name='参考链接'),
        ),
    ]
