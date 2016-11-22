# -*- coding:utf-8 -*-

from django import forms
from .models import Article,Category,Bash,Video,SoftWare,Course,CourseField

from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


import copy

class AddBlog(forms.ModelForm):
    '''url:http://blog.chinaunix.net/uid-21633169-id-4349923.html
       url2:https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
    '''
    class Meta:
        '''关联类'''
        model=Article
        exclude = ('user',)

class AddBash(forms.ModelForm):
    class Meta:
        model=Bash
        fields=['title','categeory','content']

class AddVideo(forms.ModelForm):
    class Meta:
        model=Video
        exclude = ('user',)

class AddSoft(forms.ModelForm):
    class Meta:
        model=SoftWare
        exclude = ('user',)

class AddCourse(forms.ModelForm):
    class Meta:
        model=Course
        fields = ['title']
        #exclude = ('software','user',)
        #exclude = ()

class AddCourseField(forms.ModelForm):
    class Meta:
        model = CourseField
        exclude = ('course','user',)

class EditCourseField(forms.ModelForm):
    class Meta:
        model = CourseField
        exclude = ('user',)

class EditCourse(forms.ModelForm):
    class Meta:
        model=Course
        exclude = ('user',)

class Reg(forms.ModelForm):
    '''参考:http://stackoverflow.com/questions/5827590/css-styling-in-django-forms'''
    class Meta:
        model=User
        #exclude = ()
        fields=['username','password','email']
        widgets = {
            'password':forms.TextInput(attrs={'type': 'password'})
        }
###同AddBlog，废弃
# class EditBlog(forms.ModelForm):
#     '''https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/#django.forms.ModelForm'''
#     class Meta:
#         '''创建类'''
#         model=Article
#         fields = ['title','categeory','image_url_i','content']
