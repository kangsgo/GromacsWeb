## Gromacs中文介绍
Gromacs中文社区是一个为分子模拟在线交流制作的开源社区，基于Python3.5以及Django1.84制作，实测Django1.10无法使用，其它版本未做测试。

## 功能概要

发布博客/视频/教程/脚本

集成ckeditor编辑器，上传图片

用户登录注册

发表相关主题二级主题

## 安装使用
### 1.依赖环境

```
Python3.5
Django==1.84
Pillow==3.4.2
Django-ckeditor==5.1.1
```

### 2.快速安装

```bash
git clone https://github.com/kangsgo/GromacsWeb.git
pip3 install -r requirement.txt
```

### 3.测试安装

构建virtulenv虚拟环境

```bash
source py3env/bin/active
```
克隆到本地

```bash
git clone https://github.com/kangsgo/GromacsWeb.git
```
安装依赖

```bash
git clone https://github.com/kangsgo/GromacsWeb.git
pip3 install -r requirement.txt
```
设置
```bash
cd GromacsWeb/
python manager.py makemigrations
python manager.py migrate
python manager.py createsuperuser
```

### 4.环境部署
建议参考Nginx + Gunicorn + Django 部署小记

链接：http://www.isaced.com/post-248.html

## 更新日志

2016-12-23 version 1.0

## 预览

### 1.在线预览

gromacs中文社区：http://www.gromacs.cn

## 联系

kangsgo@163.com 小康


