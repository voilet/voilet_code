#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================
import re
from django.core.mail import send_mail
from django import forms

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext
import commands

def index(requst):
    salt_status = commands.getoutput("salt-run manage.status")
    #业务列表
    #return render_to_response('test.html',{'title':"运维报障系统－－－故障列表页",'contacts':salt_status},context_instance=RequestContext(requst))
    print salt_status.up
    return render_to_response('test.html',{'title':"运维报障系统－－－故障列表页",'contacts':salt_status})

