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
import json,time
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from server_idc.models import  Host,IDC,Server_System,Cores,System_os,system_arch,MyForm,System_usage
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

from django.contrib.auth.models import User

from salt_ui.api.salt_token_id import *
from salt_ui.api.salt_https_api import salt_api_jobs
from mysite.settings import  salt_api_pass,salt_api_user,salt_api_url
#日志记录
from salt_ui.log_class.api_log_class import salt_log

class Host_from(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = MyForm.objects.values_list("id","service_name")
    # print FAVORITE_COLORS_CHOICES
    business = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = Host

@login_required
@csrf_protect
def server_update(request,id):
    context = {}
    edit_id = Host.objects.get(id = id)
    #机房名称
    idc_name = IDC.objects.all()
    server_type = MyForm.objects.all()
    if request.method == 'POST':    #验证post方法
        uf = Host_from(request.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            uf.auto_id = edit_id.id
            zw = uf.save(commit=False)
            zw.edit_username = request.user.username
            zw.old_editname = edit_id.edit_username
            zw.old_editdatetime = edit_id.edit_datetime
            zw.create_time = edit_id.create_time
            zw.id=edit_id.id
            zw.save()
            uf.save_m2m()
            print "保存数据"
            return HttpResponseRedirect('/assets/list_id/'+id)
        else:
            print "is over"
            print uf.is_valid()
    else:
        uf = Host_from()
        context["uf"] = uf
        context["edit_brand"] = Server_System
        context["edit_Cores"] = Cores
        context["edit_system"] = System_os
        context["edit_system_arch"] = system_arch
        context["server_type"] = server_type
        context["edit_id"] = edit_id
        context["server_name"] = idc_name
        context["edit_usage"] = System_usage
        token_api_id = token_id()
        list_all = salt_api_token(
        {
        # 'client': 'local',
        'fun': 'grains.items',
        'tgt':edit_id.node_name,
        # 'arg':salt_cmd_lr ,
                       },
        salt_api_url,
        {"X-Auth-Token": token_api_id}
        )
        list_all = list_all.run()
        for i in list_all["return"]:
            try:
                context["jid"] =  i["jid"]
                context["minions"] = i["minions"]
            except KeyError:
                return render_to_response('server_idc/update_error.html',context,context_instance=RequestContext(request))
        jobs_id = context["jid"]
        jobs_url = salt_api_url + "/jobs/" + jobs_id
        minions_list_all = salt_api_jobs(
        jobs_url,
        {"X-Auth-Token": token_api_id}
        )
        voilet_test = minions_list_all.run()
        for i in voilet_test["return"]:
            update_keys = i.keys()
            try:
                update_key = update_keys[0]
            except IndexError:
                return render_to_response('server_idc/update_error.html',context,context_instance=RequestContext(request))
            context["cmd_run"] = i[update_key]
        context["eth0"] = context["cmd_run"]["ip_interfaces"]["eth0"][0]
        try:
            if context["cmd_run"]["ip_interfaces"]["eth1"]:
                context["eth1"] = context["cmd_run"]["ip_interfaces"]["eth1"][0]
        except KeyError:
            context["eth1"] = False
        context["mem_total"] = context["cmd_run"]["mem_total"]
        context["num_cpus"] = int(context["cmd_run"]["num_cpus"])
        context["osarch"] = context["cmd_run"]["osarch"]
        context["cpu_model"] = context["cmd_run"]["cpu_model"]
        context.update(csrf(request))
        # print yaml.dump(context["cmd_run"])
        #日志入库
        return render_to_response('server_idc/update.html',context,context_instance=RequestContext(request))


