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

class Service(models.Model):
    name = models.CharField(max_length=50)
    target = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'service'

class Script(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    args = models.CharField(max_length=100)
    public = models.CharField(max_length=5)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'script'

