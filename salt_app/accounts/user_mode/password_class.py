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
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from accounts.models import UserCreateForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# @login_required
def edit_password(request):
    return render_to_response('edit_passwd.html',)