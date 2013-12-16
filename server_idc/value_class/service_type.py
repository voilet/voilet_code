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

import json,time,urllib
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
from salt_ui.api.salt_https_api import salt_api_jobs,pxe_api
from mysite.settings import  salt_api_pass,salt_api_user,salt_api_url,pxe_url_api

class Host_from(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = MyForm.objects.values_list("id","service_name")
    # print FAVORITE_COLORS_CHOICES
    business = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = Host


class Service_type_from(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = User.objects.values_list("id","username")
    service_user = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = MyForm


#按服务排序
@login_required
@csrf_protect
def server_type_notnode(request):
    content = {}
    in_node = []
    not_node = []
    all_node = Host.objects.values_list("node_name")
    display = Host.objects.all()
    business_name = MyForm.objects.all()
    for i in  business_name:
        s = i.host_set.values_list("node_name")
        in_node += s
    for v in all_node:
        if v not in in_node:
            v =  u"%s" % (v)
            not_node.append(v)
    content["server_type"] = MyForm.objects.all()
    content["display"] = display
    content["no_node"] = not_node
    content.update(csrf(request))
    return render_to_response('server_idc/service_no_type.html',content,context_instance=RequestContext(request))

#业务删除
@login_required
@csrf_protect
def auth_server_type_delete(request):
    content = {}
    if request.method == 'POST':    #验证post方法
        uf = Service_type_from(request.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            uf.save()
            uf = Service_type_from()
            content['uf'] = uf
            content["server_type"] = MyForm.objects.all()
            content.update(csrf(request))
            return render_to_response('server_idc/server_type_del.html',content,context_instance=RequestContext(request))
        else:
            print "save error"
            uf = Service_type_from()
            content["server_type"] = MyForm.objects.all()
            content['uf'] = uf
            content.update(csrf(request))
            return render_to_response('server_idc/server_type_del.html',content,context_instance=RequestContext(request))
    else:
        business_name = MyForm.objects.all().order_by("-id")
        list_api_return = []
        for i in business_name:
            server_list = i.host_set.all()
            server_user_all = i.service_user.all()
            user = request.user.myform_set.all()
            content["server_type"] = MyForm.objects.all()
            content["list"] = server_list
            content["server_user_all"] = server_user_all
            content["business_name"] = business_name
            list_api_return.append({"server_user_all":server_user_all,"server_type":i,"type_id":i.id})
        if len(content['list']) >0:
            content["test_error"] = True
        else:
            content["test_error"] = False
        content["list_server_type"] = list_api_return
        content["server_type"] = MyForm.objects.all()
        content.update(csrf(request))
        return render_to_response('server_idc/server_type_del.html',content,context_instance=RequestContext(request))

