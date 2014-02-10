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
def auth_server_type_delete(request,id):
   if MyForm.objects.filter(id=id).count() > 0:
        # id_servername = MyForm.objects.get(id=id)
        # del_username = User.objects.get(username=request.session["auth_username"])
        # idc_log(request.session["auth_username"], id_servername.service_name,"业务删除", request.session["auth_username"], time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), id, del_username.id)
        MyForm.objects.get(id=id).delete()
        content = {}
        content.update(csrf(request))
        return HttpResponseRedirect("/assets/server/type/list/")

