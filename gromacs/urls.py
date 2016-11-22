# -*- coding:utf-8 -*-
from django.conf.urls import url



urlpatterns = [
    #首页
    url(r'^$', 'gromacs.views.index', name='index'),

    #博客大类
    url(r'^blog/$','gromacs.views.blog',name='blog_index'),
    url(r'^blog/(?P<blog_id>\d+)$','gromacs.views.blog_detail',name='blog_detail'),
    url(r'^blog/add/$','gromacs.views.blog_add',name="blog_add"),
    url(r'^blog/(?P<blog_id>\d+)/edit/$','gromacs.views.blog_edit',name="blog_edit"),
    url(r'^blog/(?P<blog_id>\d+)/delete/$','gromacs.views.blog_delete',name="blog_delete"),

    url(r'^software/$','gromacs.views.software',name='software_index'),
    url(r'^software/(?P<software_id>\d+)$','gromacs.views.software_detail',name='software_detail'),
    url(r'^software/add/$','gromacs.views.soft_add',name="soft_add"),
    url(r'^software/(?P<soft_id>\d+)/edit/$','gromacs.views.soft_edit',name="soft_edit"),
    url(r'^software/(?P<soft_id>\d+)/delete/$','gromacs.views.soft_delete',name="soft_delete"),

    # 教程详细页面
    url(r'^software/(?P<software_id>\d+)/(?P<course_id>\d+)$','gromacs.views.course_detail',name='course_detail'),
    url(r'^software/(?P<software_id>\d+)/add/$','gromacs.views.course_add',name="course_add"),
    # 增加教程小段
    url(r'^software/(?P<software_id>\d+)/(?P<course_id>\d+)/add/$','gromacs.views.coursefield_add',name="coursefield_add"),
    url(r'^course/(?P<coursefield_id>\d+)/edit/$','gromacs.views.coursefield_edit',name="coursefield_edit"),
    url(r'^course/(?P<coursefield_id>\d+)/delete/$','gromacs.views.coursefield_delete',name="coursefield_delete"),
    url(r'^software/(?P<software_id>\d+)/(?P<course_id>\d+)/edit/$','gromacs.views.course_edit',name="course_edit"),
    url(r'^software/(?P<software_id>\d+)/(?P<course_id>\d+)/delete/$','gromacs.views.course_delete',name="course_delete"),

    #脚本页面
    url(r'^bash/$','gromacs.views.bash',name='bash_index'),
    url(r'^bash/(?P<bash_id>\d+)$','gromacs.views.bash_detail',name='bash_detail'),
    url(r'^bash/add/$','gromacs.views.bash_add',name="bash_add"),
    url(r'^bash/(?P<bash_id>\d+)/edit/$','gromacs.views.bash_edit',name="bash_edit"),
    url(r'^bash/(?P<bash_id>\d+)/delete/$','gromacs.views.bash_delete',name="bash_delete"),

    url(r'^video/$','gromacs.views.video',name='video_index'),
    url(r'^video/(?P<video_id>\d+)$','gromacs.views.video_detail',name='video_detail'),
    url(r'^video/add/$','gromacs.views.video_add',name="video_add"),
    url(r'^video/(?P<video_id>\d+)/edit/$','gromacs.views.video_edit',name="video_edit"),
    url(r'^video/(?P<video_id>\d+)/delete/$','gromacs.views.video_delete',name="video_delete"),

    #注册页面
    url(r'^reg/$','gromacs.views.reg',name='reg'),
    
    #个人主页
    url(r'^accounts/profile/$', 'gromacs.views.profile',name="profile"),
]