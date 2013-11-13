#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2013-02-20 14:52:11
#      History:
#=============================================================================

from django.db import models


# Create your models here.

from op.models import *
from django.contrib import admin

class Post(models.Model):
    # user_name = models.ForeignKey('Poster',blank=True,null=True,verbose_name='姓名')
    user_name = models.CharField(max_length=14,blank=True,null=True,verbose_name='用户名')
    fault_type = models.ForeignKey('Poster_type',blank=True,null=True,verbose_name='故障类型')
    Source = models.ForeignKey('Poster_Source',blank=True,null=True,verbose_name='报障来原')
    title = models.CharField(max_length=64,blank=True,null=True,verbose_name='故障描述')
    Occur_date = models.DateTimeField(verbose_name='发生时间')
    Discovery_date = models.DateTimeField(verbose_name='发现时间')
    Solve_date = models.DateTimeField(blank=True,null=True,verbose_name='解决时间')
    content = models.TextField(max_length=20480,blank=True,null=True,verbose_name='处理过程分析')
    user_id = models.IntegerField(max_length=6,blank=True,null=True,verbose_name='用户id')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "报障"



class Poster_type(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "故障类型"

class Poster_Source(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "报障来源"

class PostAdmin(admin.ModelAdmin):
    list_display = ('user_name','title','Discovery_date','Occur_date','Solve_date','Source')
    search_fields = ('title','user_name')


class PosterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email')

class Poster_OP(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Poster_type, Poster_OP)
admin.site.register(Poster_Source, Poster_OP)












