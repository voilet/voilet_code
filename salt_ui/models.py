#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#      History:
#=============================================================================
from django.db import models
from django import forms

from django.db import models


class returns(models.Model):
    fun = models.CharField(max_length=50,blank=True,null=True)
    jid = models.CharField(max_length=255,blank=True,null=True)
    fun_return = models.TextField(blank=True,null=True)
    node_id = models.CharField(max_length=64,blank=True,null=True)
    success = models.CharField(max_length=10,blank=True,null=True)
    full_ret = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"salt上报"
        verbose_name_plural = verbose_name

class salt_api_log(models.Model):
    user_name = models.CharField(max_length="20",verbose_name="用户名")
    minions = models.CharField(max_length="2048",verbose_name="主机名")
    jobs_id = models.CharField(max_length="40",verbose_name="job")
    stalt_type = models.CharField(max_length="20",verbose_name="操作类型")
    salt_len_node = models.IntegerField(max_length="20",verbose_name="多少台主机执行")
    stalt_input = models.CharField(max_length="100",blank=True,null=True,verbose_name="命令")
    api_return = models.TextField(verbose_name="执行记录")
    log_time = models.DateTimeField(auto_now=True,verbose_name="操作时间")
    def __unicode__(self):
        return self.user_name
    class Meta:
        verbose_name = u"salt操作日志"
        verbose_name_plural = verbose_name
