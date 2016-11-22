# -*- coding:utf-8 -*-
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value,arg):
    '''https://shenxgan.gitbooks.io/django/content/publish/2015-08-03-django-user-login-style.html'''
    return value.as_widget(attrs={'class':arg})

@register.filter(name='add_type')
def add_type(value,arg):
    '''https://shenxgan.gitbooks.io/django/content/publish/2015-08-03-django-user-login-style.html'''
    return value.as_widget(attrs={'type':arg})

@register.filter(name='add_placeholder')
def add_placeholder(value,arg):
    '''https://shenxgan.gitbooks.io/django/content/publish/2015-08-03-django-user-login-style.html'''
    return value.as_widget(attrs={'placeholder':arg})
# 方法2

# http://stackoverflow.com/questions/5827590/css-styling-in-django-forms

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         widgets = {
#             'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
#         }