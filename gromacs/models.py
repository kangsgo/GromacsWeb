# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
#分类
class Category(models.Model):
    title = models.CharField(max_length = 50, verbose_name='分类名称') #分类名称

    class Meta:
        verbose_name = '分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title



# 软件
class SoftWare(models.Model):
    user = models.ForeignKey(User, related_name='softuser') #软件发布人
    title = models.CharField(max_length = 100, verbose_name='标题') #软件题目
    categeory = models.ForeignKey(Category, verbose_name='分类') #分类
    url   = models.URLField(blank = True, null = True,verbose_name='链接') #软件官网链接
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #软件日期
    content = RichTextUploadingField(blank = True,null=True,verbose_name='正文') #博客正文

    class Meta:
        verbose_name = '软件'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title

# 教程
class Course(models.Model):
    user = models.ForeignKey(User, related_name='courseuser') #教程发布人
    software = models.ForeignKey(SoftWare, verbose_name='软件') #为何种软件教程
    title = models.CharField(max_length = 100, verbose_name='教程') #教程
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #教程日期

    class Meta:
        verbose_name = '教程'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title

# 教程小段
class CourseField(models.Model):
    user = models.ForeignKey(User, related_name='coursefielduser') #教程小段发布人
    course = models.ForeignKey(Course) #继承小段
    tags = models.CharField(max_length = 50, verbose_name='标签') #小标签
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #教程日期
    content = RichTextUploadingField(blank = True,null=True,verbose_name='内容') #小内容

    class Meta:
        verbose_name = '教程小段'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.tags


# 视频
class Video(models.Model):
    user = models.ForeignKey(User, related_name='videouser') #视频发布人
    software = models.ForeignKey(SoftWare, verbose_name='软件') #为何种软件视频
    title = models.CharField(max_length = 100, verbose_name='视频题目') #视频题目
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #软件日期
    image_url_i = models.ImageField(upload_to='video/%Y',null=True,verbose_name='图片') #软件图片
    abstact = RichTextUploadingField(blank = True, null = True, verbose_name='简介') #视频

    class Meta:
        verbose_name = '视频'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title

# 博客
class Article(models.Model):
    user = models.ForeignKey(User, related_name='bloguser') #博客发布人
    title = models.CharField(max_length = 100, verbose_name='博客标题')  #博客题目
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #文章日期
    categeory = models.ForeignKey(Category, verbose_name='分类') #博客分类
    image_url_i = models.ImageField(upload_to='article/%Y',blank=True,null=True,verbose_name='图片') #博客预览图
    content = RichTextUploadingField(blank = True, null = True, verbose_name='内容') #博客内容
    reference = models.ForeignKey('ReferenceLink',blank=True,null=True,verbose_name='参考链接') #博客参考链接

    class Meta:
        verbose_name = '博客'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title

# 参考链接
class ReferenceLink(models.Model):
    title = models.CharField(max_length = 100, verbose_name='标题') #链接题目
    url   = models.URLField(blank = True, null = True,verbose_name='链接') #链接网址

    class Meta:
        verbose_name = '参考链接'
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.title

# 脚本
class Bash(models.Model):
    user = models.ForeignKey(User, related_name='bashuser') #脚本发布人
    title = models.CharField(max_length = 100, verbose_name='标题') #脚本名称
    categeory = models.ForeignKey(Category, verbose_name='分类') #分类
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #脚本日期
    content = RichTextUploadingField(blank = True,null=True,verbose_name='正文') #脚本内容

    class Meta:
        verbose_name = '脚本'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title

# 其他页面
class Page(models.Model):
    title = models.CharField(max_length = 50 , verbose_name='页面标题') #页面标题
    order = models.IntegerField(default=1,verbose_name= '页面顺序') #页面顺序
    content = models.TextField(blank = True, null=True, verbose_name='页面内容') #页面内容

    class Meta:
        verbose_name = '页面'
        verbose_name_plural=verbose_name
        ordering = ['order']

    def __str__(self):
        return self.title

# 网站链接
class WebLink(models.Model):
    title = models.CharField(max_length = 50 , verbose_name='网站标题')
    linkategeory = models.ForeignKey(Category, verbose_name='分类') #分类
    date_time = models.DateTimeField(auto_now_add = True, verbose_name='日期') #网站日期
    url   = models.URLField(blank = True, null = True,verbose_name='链接') #链接网址
    content = models.CharField(max_length = 200 , verbose_name='简介') #简介

    class Meta:
        verbose_name = '网站链接'
        verbose_name_plural=verbose_name
        ordering = ['-date_time']

    def __str__(self):
        return self.title