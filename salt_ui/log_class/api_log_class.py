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

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db import connection
from django.http import HttpResponse
#from salt_ui.api import salt_api
from salt_ui.models import *
from django.contrib.auth.decorators import login_required
import commands,json,yaml
import subprocess
from salt_ui.api import *
from salt_ui.models import salt_api_log
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from salt_ui.api.salt_token_id import salt_api_token
from salt_ui.api.salt_token_id import *
from salt_ui.api.salt_https_api import salt_api_jobs
from mysite.settings import  salt_api_pass,salt_api_user,salt_api_url
import ast
class OP_From(forms.ModelForm):
    class Meta:
        model = salt_api_log


def salt_log(user_name, minions, jobs_id, salt_type, len_salt_node, salt_cmd_lr, api_return):
    salt_shell_logs = salt_api_log(user_name=user_name, minions=minions, jobs_id=jobs_id, stalt_type=salt_type, salt_len_node=len_salt_node, stalt_input=salt_cmd_lr, api_return=api_return,)
    salt_shell_logs.save()


@login_required
@csrf_protect
def salt_data_log(request):
     context = {}
     list_api_return = []
     log_list = salt_api_log.objects.all().order_by("-id")
     for i in log_list:
         api_return = ast.literal_eval(i.api_return)
         minions = ast.literal_eval(i.minions)
         list_api_return.append({"api_return":api_return, "minions":minions, "log_time":i.log_time, "username":i.user_name, "jobs_id":i.jobs_id, "id":i.id, "stalt_type":i.stalt_type, "stalt_input":i.stalt_input, "salt_len_node":i.salt_len_node})
     context["log"] = list_api_return
     context.update(csrf(request))
     return render_to_response('saltstack/salt_log.html',context,context_instance=RequestContext(request))

#判断选择了多少台主机
# @login_required
# @csrf_protect
# def salt_data_log(request):
#      context = {}
#      list_api_return = []
#      log_list = salt_api_log.objects.all().order_by("-id")
#      for i in log_list:
#          api_return = ast.literal_eval(i.api_return)
#          minions = ast.literal_eval(i.minions)
#          list_api_return.append({"api_return":api_return, "minions":minions, "log_time":i.log_time, "username":i.user_name, "jobs_id":i.jobs_id, "id":i.id, "stalt_type":i.stalt_type, "stalt_input":i.stalt_input, "salt_len_node":i.salt_len_node})
#      context["log"] = list_api_return
#      context.update(csrf(request))
#      return render_to_response('saltstack/salt_log.html',context,context_instance=RequestContext(request))