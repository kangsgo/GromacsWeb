# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

#视图
#from django.views.generic import ListView
#from django.views.generic.edit import FormView
from .forms import AddBlog,AddBash,AddVideo,AddSoft,AddCourse,EditCourse,Reg,AddCourseField,EditCourseField
#用户登陆 url:http://www.loonapp.com/blog/19/
from django.contrib.auth.decorators import login_required
#导入设置
from django.conf import settings
from gromacs.models import Article,SoftWare,Bash,Video,Course,CourseField,Category
from django.contrib.auth.models import User


#-------首页-------

# Create your views here.
def index(request):
    content={}
    return render(request,'index.html',content)

#-------页面系统-------

###########################################
##             软件页面                   ##
###########################################

# 1 软件页面
def software(request):
    soft=SoftWare.objects.all()
    MEDIA_URL = settings.MEDIA_URL
    content = {'soft':soft,"MEDIA_URL":MEDIA_URL}
    return render(request,'soft_index.html',content)

# 2 添加软件页面
@login_required
def soft_add(request):
    if request.method=='POST':
        user=SoftWare(user=request.user)
        form=AddSoft(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('software_index'))
    else:
        form=AddSoft()
    return render(request,"soft_add.html",{'form':form})

# 3 软件内容页面
def software_detail(request,software_id):
    soft= SoftWare.objects.get(id=str(software_id))
    course = Course.objects.filter(software=soft).order_by('date_time') #按照时间顺序排列
    MEDIA_URL = settings.MEDIA_URL
    content = {'soft':soft,'course':course,"MEDIA_URL":MEDIA_URL}
    return render(request,'soft_detail.html',content)

# 4 编辑软件页面
@login_required
def soft_edit(request,soft_id):
    softid=SoftWare.objects.get(pk=soft_id)
    if not softid.user == request.user:
        return HttpResponse("非本人发布软件")
    if request.method=='POST':
        form=AddSoft(request.POST,request.FILES, instance=softid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('software_index'))
    else:
        form=AddSoft(instance=softid)
    return render(request,"soft_add.html",{'form':form,'soft_id':soft_id})

# 5 删除软件页面
@login_required
def soft_delete(request,soft_id):
    softid=SoftWare.objects.get(pk=soft_id)
    if not softid.user == request.user:
        return HttpResponse("非本人发布软件")
    try:
        soft_delete=SoftWare.objects.get(pk=soft_id)
        soft_delete.delete()
        return HttpResponseRedirect(reverse('software_index'))
    except Exception as e:
        return HttpResponse(e)


###########################################
##             软件教程页面               ##
###########################################

# 1 增加教程页面
@login_required
def course_add(request,software_id):
    '''url:https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/'''
    if request.method=='POST':
        softid = SoftWare.objects.get(pk=software_id)
        course = Course(software=softid,user=request.user)
        form=AddCourse(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('soft_index'))
    else:
        form=AddCourse()
    return render(request,"course_add.html",{'form':form,'software_id':software_id})

# 2 教程内容页面
def course_detail(request,software_id,course_id):
    course= Course.objects.get(id=str(course_id))
    softcourse = Course.objects.filter(software=software_id).order_by('date_time') 
    coursefeild = CourseField.objects.filter(course=course).order_by('date_time') 
    MEDIA_URL = settings.MEDIA_URL
    content = {'course':course,'MEDIA_URL':MEDIA_URL,'coursefeild':coursefeild,'softcourse':softcourse,'software_id':software_id,'course_id':course_id}
    return render(request,'course_detail.html',content)

# 3 编辑教程内容页面
@login_required
def course_edit(request,software_id,course_id):
    courseid=Course.objects.get(pk=course_id)
    if not courseid.user == request.user:
        return HttpResponse("非本人发布教程")
    if request.method=='POST':
        form=EditCourse(request.POST,instance=courseid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('soft_index'))
    else:
        form=EditCourse(instance=courseid)
    return render(request,"course_add.html",{'form':form,'software_id':software_id,'course_id':course_id})
 
# 4 删除教程内容页面
@login_required
def course_delete(request,course_id):
    courseid=Course.objects.get(pk=course_id)
    if not courseid.user == request.user:
        return HttpResponse("非本人发布教程")
    try:
        course_delete=Course.objects.get(pk=course_id)
        course_delete.delete()
        return HttpResponseRedirect(reverse('soft_index'))
    except Exception as e:
        return HttpResponse(e)

# 5 增加教程小段
@login_required
def coursefield_add(request,software_id,course_id):
    '''url:https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/'''
    if request.method=='POST':
        softid = Course.objects.get(id=course_id)
        course = CourseField(course=softid,user=request.user)
        form=AddCourseField(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form=AddCourseField()
    return render(request,"coursefield_add.html",{'form':form,'software_id':software_id,'course_id':course_id})

# 6 删除教程小段内容页面
@login_required
def coursefield_delete(request,coursefield_id):
    coursefieldid=CourseField.objects.get(pk=coursefield_id)
    if not coursefieldid.user == request.user:
        return HttpResponse("非本人发布教程小段")
    try:
        coursefield_delete=CourseField.objects.get(pk=coursefield_id)
        coursefield_delete.delete()
        return HttpResponseRedirect(reverse('profile'))
    except Exception as e:
        return HttpResponse(e)

# 7 编辑教程小段内容页面
@login_required
def coursefield_edit(request,coursefield_id):
    courseid=CourseField.objects.get(pk=coursefield_id)
    if not courseid.user == request.user:
        return HttpResponse("非本人发布教程小段")
    if request.method=='POST':
        form=EditCourseField(request.POST,instance=courseid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form=EditCourseField(instance=courseid)
    return render(request,"coursefield_add.html",{'form':form,'coursefield_id':coursefield_id})

# # 6 编辑教程小段
# @login_required
# def coursefield_edit(request,software_id,course_id):
#     '''url:https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/'''
#     if request.method=='POST':
#         softid = Course.objects.get(id=course_id)
#         course = CourseField(course=softid,user=request.user)
#         form=AddCourseField(request.POST,instance=course)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("成功")
#     else:
#         form=AddCourseField()
#     return render(request,"coursefield_add.html",{'form':form,'software_id':software_id,'course_id':course_id})



###########################################
##             博客页面                   ##
###########################################

# 1 博客首页
def blog(request):
    categeory=Category.objects.all()
    post = Article.objects.all()
    MEDIA_URL = settings.MEDIA_URL
    content ={'post':post,'MEDIA_URL':MEDIA_URL,'categeory':categeory}
    return render(request,'blog_index.html',content)
# 采用通用视图
# url:https://shenxgan.gitbooks.io/django/content/publish/2015-08-06-blog-index-articlelist.html
#class BlogListView(ListView):
#    template_name = 'blog_index.html'
#    model = Article

# 2 博客内容页面
def blog_detail(request,blog_id):
    categeory=Category.objects.all()
    post= Article.objects.get(id=str(blog_id))
    MEDIA_URL = settings.MEDIA_URL
    content = {'post':post,'MEDIA_URL':MEDIA_URL,'categeory':categeory}
    return render(request,'blog_detail.html',content)

# 3 创建博客页面
@login_required
def blog_add(request):
    if request.method=='POST':
        user=Article(user=request.user)
        form=AddBlog(request.POST,request.FILES,instance=user)
        #form.image_url_i = request.Files['image_url_i']
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form=AddBlog()
    return render(request,"blog_add.html",{'form':form})

# 4 编辑博客页面
@login_required
def blog_edit(request,blog_id):
    blogid=Article.objects.get(pk=blog_id)
    if not blogid.user == request.user:
        return HttpResponse("非本人发布博客")
    if request.method=='POST':
        form=AddBlog(request.POST,request.FILES, instance=blogid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form=AddBlog(instance=blogid)
    return render(request,"blog_add.html",{'form':form,'blog_id':blog_id})

# 5 删除博客页面
@login_required
def blog_delete(request,blog_id):
    blogid=Article.objects.get(pk=blog_id)
    if not blogid.user == request.user:
        return HttpResponse("非本人发布博客")
    try:
        blog_delete=Article.objects.get(pk=blog_id)
        blog_delete.delete()
        return HttpResponseRedirect(reverse('blog_index'))
    except Exception as e:
        return HttpResponse(e)


###########################################
##             脚本页面                   ##
###########################################

# 1 脚本首页
def bash(request):
    bash = Bash.objects.all()
    content ={'bash':bash}
    return render(request,'bash_index.html',content)

# 2 添加脚本页面
@login_required
def bash_add(request):
    if request.method=='POST':
        user=Bash(user=request.user)
        form=AddBash(request.POST,request.user,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bash_index'))
    else:
        form=AddBash()
    return render(request,"bash_add.html",{'form':form})

#  3 脚本内容页面
def bash_detail(request,bash_id):
    bash= Bash.objects.get(id=str(bash_id))
    content = {'bash':bash}
    return render(request,'bash_detail.html',content)

#  4 编辑脚本页面
@login_required
def bash_edit(request,bash_id):
    bashid=Bash.objects.get(pk=bash_id)
    if not bashid.user == request.user:
        return HttpResponse("非本人发布脚本")
    if request.method=='POST':
        form=AddBash(request.POST,request.FILES, instance=bashid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bash_index'))
    else:
        form=AddBash(instance=bashid)
    return render(request,"bash_add.html",{'form':form,'bash_id':bash_id})

# 5 删除脚本页面
@login_required
def bash_delete(request,bash_id):
    bashid=Bash.objects.get(pk=bash_id)
    if not bashid.user == request.user:
        return HttpResponse("非本人发布脚本")
    try:
        bash_delete=Bash.objects.get(pk=bash_id)
        bash_delete.delete()
        return HttpResponseRedirect(reverse('bash_index'))
    except Exception as e:
        return HttpResponse(e)

###########################################
##             视频页面                   ##
###########################################

#1 视频首页
def video(request):
    video = Video.objects.all()
    MEDIA_URL = settings.MEDIA_URL
    content ={'video':video,'MEDIA_URL':MEDIA_URL}
    return render(request,'video_index.html',content)

# 2 添加视频页面
@login_required
def video_add(request):
    if request.method=='POST':
        user=Video(user=request.user)
        form=AddVideo(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('video_index'))
    else:
        form=AddVideo()
    return render(request,"video_add.html",{'form':form})

# 3 视频内容页面
def video_detail(request,video_id):
    video= Video.objects.get(id=str(video_id))
    content = {'video':video}
    return render(request,'video_detail.html',content)

#  4 编辑视频页面
@login_required
def video_edit(request,video_id):
    videoid=Video.objects.get(pk=video_id)
    if not videoid.user == request.user:
        return HttpResponse("非本人发布视频")
    if request.method=='POST':
        form=AddVideo(request.POST,request.FILES, instance=videoid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('video_index'))
    else:
        form=AddVideo(instance=videoid)
    return render(request,"video_add.html",{'form':form,'video_id':video_id})

# 5 删除视频页面
@login_required
def video_delete(request,video_id):
    videoid=Video.objects.get(pk=video_id)
    if not videoid.user == request.user:
        return HttpResponse("非本人发布视频")
    try:
        video_delete=Video.objects.get(pk=video_id)
        video_delete.delete()
        return HttpResponseRedirect(reverse('video_index'))
    except Exception as e:
        return HttpResponse(e)

#---登录系统---

# https://docs.djangoproject.com/en/1.8/topics/auth/default/

# 2 注册页面
def reg(request):
    '''参考以下两个链接：
    http://www.cnblogs.com/fnng/p/3744099.html
    https://github.com/ericls/niji/blob/master/niji/views.py
    '''
    if request.method=='POST':
        form=Reg(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            return HttpResponseRedirect(reverse('profile'))
    else:
        form=Reg()
    return render(request,"registration/reg.html",{'form':form})

@login_required
def profile(request):
    soft=SoftWare.objects.filter(user=request.user).order_by('date_time')
    blog=Article.objects.filter(user=request.user).order_by('date_time')
    bash=Bash.objects.filter(user=request.user).order_by('date_time')
    video=Video.objects.filter(user=request.user).order_by('date_time')
    course=Course.objects.filter(user=request.user).order_by('date_time')
    coursefield=CourseField.objects.filter(user=request.user).order_by('date_time')
    content={'soft':soft,'blog':blog,'bash':bash,'video':video,'course':course,'coursefield':coursefield}
    return render(request,"registration/profile.html",content)
