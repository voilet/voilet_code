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

from django import forms
from django.db import models


class finotify(models.Model):
    '''
    上报信息
    '''
    file_path = models.CharField(max_length=64,blank=True, null=True,verbose_name='可疑文件')
    dangerous = models.TextField(blank=True, null=True,verbose_name='报警内容 ')
    server_ip = models.CharField(blank=True, null=True,max_length=64,verbose_name='服务器ip')
    files_create_time = models.DateTimeField(blank=True, null=True,max_length=64,verbose_name='监控时间')


class hacker_url(models.Model):
    '''
    黑客入侵上报信息
    '''
    code_url = models.TextField(max_length=1024,blank=True, null=True,verbose_name='攻击地址')
    server_ip = models.CharField(blank=True, null=True,max_length=64,verbose_name='服务器ip')
    user_ip = models.CharField(blank=True, null=True,max_length=64,verbose_name='攻击者ip')
    hacker_time = models.DateTimeField(blank=True, null=True,max_length=64,verbose_name='攻击时间')
    Client_Information = models.CharField(max_length=1024,verbose_name='客户端信息')
    hack_city = models.CharField(max_length=128,verbose_name='省/市')
    hack_city_addr = models.CharField(max_length=128,blank=True,null=True,verbose_name='地区')

class naxsi_hacker(models.Model):
    '''
    naxsi黑客入侵上报信息
    Type_attack,hack_exp_id,hack_url_code,server_ip,hack_ip,Detailed,hacker_city,hacker_Area,hacker_time
    '''
    type_attack = models.CharField(max_length=12,blank=True, null=True,verbose_name='攻击类型')
    hack_exp_id = models.CharField(blank=True, null=True,max_length=64,verbose_name='攻击类型ID')
    hack_url_code = models.TextField(max_length=1024,blank=True, null=True,verbose_name='提交参数')
    server_ip = models.CharField(blank=True, null=True,max_length=64,verbose_name='服务器IP')
    hack_ip = models.CharField(blank=True, null=True,max_length=64,verbose_name='黑客IP')
    Detailed = models.CharField(max_length=1024,verbose_name='详细信息')
    hacker_city = models.CharField(max_length=128,verbose_name='省/市')
    hacker_Area = models.CharField(max_length=128,blank=True,null=True,verbose_name='地区')
    hacker_time = models.DateTimeField(blank=True, null=True,max_length=64,verbose_name='攻击时间')
    hacker_post_get = models.CharField(max_length=12,blank=True, null=True,verbose_name='攻击方式')
    hacker_orig_url = models.CharField(max_length=12,blank=True, null=True,verbose_name='攻击地址')
    hacker_cookie = models.CharField(max_length=256,blank=True, null=True,verbose_name='cookie')
    hacker_hacker_uri = models.TextField(max_length=1024,blank=True, null=True,verbose_name='提交uri')


