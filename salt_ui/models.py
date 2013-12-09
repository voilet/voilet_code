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