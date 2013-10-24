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
from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

# Create your models here.

from assets.models import *
from django.contrib import admin



class Server_Post(models.Model):
    '''
    设置所有服务器资料录入字段
    '''
    Server_Asset_number = models.CharField(max_length=64,blank=True, null=True,verbose_name='资产编号')
    Server_eth1 = models.CharField(blank=True, null=True,max_length=64,verbose_name='网卡1')
    Server_eth2 = models.CharField(blank=True, null=True,max_length=64,verbose_name='网卡2')
    Server_Remote_control_card = models.CharField(blank=True, null=True,max_length=64,verbose_name='远控卡ip')
    Server_engine_room = models.ForeignKey('Poster',blank=True, null=True,verbose_name='所属机房')
    Server_cacti = models.CharField(blank=True, null=True,max_length=128,verbose_name='cacti_url')
    Server_Memory = models.CharField(max_length=256,blank=True, null=True,verbose_name='内存/硬盘/cpu')
    Server_Business = models.CharField(max_length=256,blank=True, null=True,verbose_name='业务')
    Server_Model = models.ForeignKey('Poster_Model',blank=True, null=True,max_length=32,verbose_name='服务器型号')
    Server_number = models.CharField(max_length=32,blank=True, null=True,verbose_name='服务器编号')
    Server_number_code = models.CharField(blank=True, null=True,max_length=32,verbose_name='快速服务代码')
    Server_number_Location = models.ForeignKey('Poster_Source',blank=True, null=True,verbose_name='机柜')
    Server_Cabinets_id = models.CharField(max_length=20,blank=True, null=True,verbose_name='机器位置')
    Server_number_Remark = models.TextField(blank=True, null=True,verbose_name='备注')
    Business = models.ManyToManyField('MyForm',blank=True, null=True,verbose_name='所属业务')

    def __unicode__(self):
        return self.Server_Asset_number
    class Meta:
        verbose_name = "添加服务器"


class Poster(models.Model):
    engine_room_name = models.CharField(max_length=30,verbose_name='机房名称')
    def __unicode__(self):
        return self.engine_room_name
    class Meta:
        verbose_name = "添加机房"

class Poster_Model(models.Model):
    Poster_Model_name = models.CharField(max_length=30,verbose_name='服务器型号')
    def __unicode__(self):
        return self.Poster_Model_name
    class Meta:
        verbose_name = "服务器型号"

class Poster_Source(models.Model):
    name = models.CharField(max_length=30,verbose_name='机柜')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "机柜"
#
class MyForm(models.Model):
    check = models.CharField(max_length=30,blank=True, null=True,verbose_name='业务')
    def __unicode__(self):
        return self.check
    class Meta:
        verbose_name = u"业务管理"





class PostAdmin(admin.ModelAdmin):
    list_display = ('Server_Asset_number','Server_eth1','Server_eth2','Server_Remote_control_card','Server_Memory','Server_Model','Server_number')
    search_fields = ('Server_Asset_number','Server_eth1','Server_eth2','Server_Model')








admin.site.register(Server_Post, PostAdmin)
admin.site.register(Poster)
admin.site.register(Poster_Source)
admin.site.register(Poster_Model)
admin.site.register(MyForm)


# admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Book)

'''
>>> server = Server_Post.objects.get(id=1)
>>> server.Business.all()
[<MyForm: api>, <MyForm: game>]

>>> b = MyForm.objects.get(check="api")
>>> b
<MyForm: api>

>>> a=b.server_post_set.all()
>>> a
[<Server_Post: FX-FWQ1273>]

'''



