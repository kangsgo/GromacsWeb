# -*- coding:utf-8 -*-

from django import forms
from .models import Article,Category

























# from ajaximage.widgets import AjaxImageWidget


# class ArticlePublishForm(forms.Form):
#     title = forms.CharField(
#         label=u'文章标题',
#         max_length=100,
#         widget=forms.TextInput(),
#     )

#     #url:http://blog.csdn.net/jw083411/article/details/8843305

#     #url:http://blog.csdn.net/kevin6216/article/details/6930524
#     #url:https://segmentfault.com/q/1010000006792490
#     #url:http://blog.csdn.net/slamx/article/details/51095066

#     # choicecategeory = Article.objects.values_list("categeory")

#     #url:http://python.usyiyi.cn/django/ref/forms/fields.html

#     # categeory = forms.ChoiceField(
#     #     label=u'分类',
#     #     widget=forms.Select(),
#     #     choices=choicecategeory,
#     # )

#     content = forms.CharField(
#         label=u'内容',
#         widget=forms.Textarea(),
#     )

#     # image_url_i = forms.ImageField(
#     #     label=u'图片',
#     #     widget=forms.CustomClearableFileInput(),
#     # )
#     # image_url_i = forms.URLField(widget=AjaxImageWidget(upload_to='form-uploads'))

#     article = Article(
#         title=title,
#         categeory=Category.objects.get(pk=1),
#         content=content,
#         # image_url_i=image_url_i,
#     )
#     article.save()

