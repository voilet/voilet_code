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

import datetime
import os
import re
#import md5
import json

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
from server_idc.models import  Host,IDC,Server_System,Cores,System_os,system_arch,MyForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from salt_ui.api.salt_token_id import salt_api_token
from salt_ui.api.salt_token_id import *
from salt_ui.api.salt_https_api import salt_api_jobs
from mysite.settings import  salt_api_pass,salt_api_user,salt_api_url,pxe_url_api

#日志记录
from salt_ui.log_class.api_log_class import salt_log


#判断选择了多少台主机
@login_required
@csrf_protect
def salt_cmd_node(request):
    context = {}
    type_node = ""
    print "*" * 100
    if request.method == 'POST':
        salt_text = request.POST
        print salt_text
        service_type = salt_text.getlist("business")
        for i in service_type:
            service_name_type = get_object_or_404(MyForm,service_name = i)
            server_list = service_name_type.host_set.all()
            for s in server_list:
                type_node += "%s," % (s.node_name)
        context["type_node"] = type_node
        print type_node
        context.update(csrf(request))
        return render_to_response('saltstack/salt_cmd_run.html',context,context_instance=RequestContext(request))
    else:
        return render_to_response('saltstack/salt_cmd_run.html',context,context_instance=RequestContext(request))