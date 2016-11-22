# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.

from gromacs.models import Category,SoftWare,Course,Video,Article,ReferenceLink,Bash,Page,WebLink,CourseField

# Register your models here.

class Courseadd(admin.StackedInline):
    model = CourseField
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [Courseadd]

admin.site.register(Category)
admin.site.register(SoftWare)
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(ReferenceLink)
admin.site.register(Bash)
admin.site.register(Page)
admin.site.register(WebLink)