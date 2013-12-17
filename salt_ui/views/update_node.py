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
from django.http import HttpResponse,HttpResponseRedirect

#日志记录
from salt_ui.log_class.api_log_class import salt_log

class Host_from(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = MyForm.objects.values_list("id","service_name")
    business = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = Host

#判断选择了多少台主机
@login_required
@csrf_protect
def salt_update_node(request):
    context = {}
    update_name = request.GET['node_name']
    if request.method == 'POST':    #验证post方法
        uf = Host_from(request.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            # uf.save()
            zw = uf.save(commit=False)
            zw.edit_username = request.user.username
            zw.save()
            uf.save_m2m()
            uf = Host_from()
            context['uf'] = uf
            context.update(csrf(request))
            return HttpResponseRedirect("/assets/server/list/")
            # return render_to_response('server_idc/index.html',context,context_instance=RequestContext(request))
        else:
            print "save error"
            uf = Host_from()
            context["server_type"] = MyForm.objects.all()
            context['uf'] = uf
            context.update(csrf(request))
            return render_to_response('server_idc/index.html',context,context_instance=RequestContext(request))

    if len(update_name) >0 and Host.objects.filter(node_name = update_name).count() == 0 :
        token_api_id = token_id()
        list = salt_api_token({'fun': 'grains.items', 'tgt':update_name}, salt_api_url, {"X-Auth-Token": token_api_id})
        master_status =list.run()
        #同步本地grains
        salt_garins_sync = salt_api_token({'fun': 'saltutil.sync_all', 'tgt':update_name, 'client':'local'}, salt_api_url, {"X-Auth-Token": token_api_id})
        salt_garins_sync.run()
        #重新加载模块
        salt_garins_reload = salt_api_token({'fun': 'sys.reload_modules', 'tgt':update_name, 'client':'local'}, salt_api_url, {"X-Auth-Token": token_api_id})
        salt_garins_reload.run()
        for i in master_status["return"]:
                context["jid"] =  i["jid"]
                context["minions"] = i["minions"]
        jobs_id = context["jid"]
        jobs_url = salt_api_url + "/jobs/" + jobs_id
        minions_list_all = salt_api_jobs(
        jobs_url,
        {"X-Auth-Token": token_api_id}
        )
        voilet_test = minions_list_all.run()
        uf = Host_from()
        for i in voilet_test["return"]:
            system_os =i[update_name]["os"]
            osarch = i[update_name]["osarch"]
            try:
                ipinfo = i[update_name]["ipinfo"]
                for mac in ipinfo:
                    mac = mac["MAC"].replace(":","-")
            except KeyError:
                mac = ""
            context["update_name"] = update_name
            context["mac"] = mac
            print context["mac"]
            context["system_os"] = system_os
            context["osarch"] = osarch
            context["uf"] = uf
            context["edit_brand"] = Server_System
            context["edit_Cores"] = Cores
            context["edit_system"] = System_os
            context["edit_system_arch"] = system_arch
            context["server_type"] = MyForm.objects.all()
            context.update(csrf(request))

        return render_to_response('saltstack/node_add.html',context,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/assets/server/list/")
        # return render_to_response('saltstack/node_add.html',context,context_instance=RequestContext(request))