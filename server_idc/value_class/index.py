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

import json,time
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from server_idc.models import  Host,IDC,Server_System,Cores,System_os,system_arch,MyForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

from django.contrib.auth.models import User


class Host_from(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = MyForm.objects.values_list("id","service_name")
    # print FAVORITE_COLORS_CHOICES
    business = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = Host

@login_required
@csrf_protect
def Index_add(request):
    content = {}
    if request.method == 'POST':    #验证post方法
        uf = Host_from(request.POST)   #绑定POST动作

        # create_time = time.strftime('%Y-%m-%d',time.localtime(time.time())) # %H:%M:%S
        if uf.is_valid(): #验证数据有效性
            uf.save()
            """
            如果commit为False,则ManyToMany就需要使用以下方法
            """
            # zw = uf.save(commit=False)
            # zw.create_time = create_time
            # zw.save()
            # uf.save_m2m()
            uf = Host_from()
            content['uf'] = uf
            content.update(csrf(request))
            return render_to_response('server_idc/index.html',content,context_instance=RequestContext(request))
        else:
            print "save error"
            uf = Host_from()
            content["server_type"] = MyForm.objects.all()
            content['uf'] = uf
            content.update(csrf(request))
            return render_to_response('server_idc/index.html',content,context_instance=RequestContext(request))
    else:
        uf = Host_from()
        #content['business'] = MyForm.objects.all()
        content['uf'] = uf
        content["server_type"] = MyForm.objects.all()
        content.update(csrf(request))
        return render_to_response('server_idc/index.html',content,context_instance=RequestContext(request))

@login_required
@csrf_protect
def list(request):
    content = {}
    server_list = Host.objects.order_by("-id")
    server_type = MyForm.objects.all()
    content["server_type"] = server_type
    content["list"] = server_list
    content.update(csrf(request))
    return render_to_response('server_idc/list.html',content,context_instance=RequestContext(request))

@login_required
@csrf_protect
def server_edit(request,id):
    content = {}
    edit_id = Host.objects.get(id = id)
    #机房名称
    idc_name = IDC.objects.all()
    server_type = MyForm.objects.all()
    if request.method == 'POST':    #验证post方法
        uf = Host_from(request.POST)   #绑定POST动作
        #print uf
        if uf.is_valid(): #验证数据有效性
            uf.auto_id = edit_id.id
            zw = uf.save(commit=False)
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
        content["uf"] = uf
        content["edit_brand"] = Server_System
        content["edit_Cores"] = Cores
        content["edit_system"] = System_os
        content["edit_system_arch"] = system_arch
        content["server_type"] = server_type
        content["edit_id"] = edit_id
        content["server_name"] = idc_name
        content.update(csrf(request))
        return render_to_response('server_idc/edit.html',content,context_instance=RequestContext(request))


#按服务排序
@login_required
@csrf_protect
def server_type_list(request,id):
    content = {}
    business_name = MyForm.objects.get(id=id)
    server_list = business_name.host_set.all()
    server_user_all = business_name.service_user.all()
    user = request.user.myform_set.all()
    print user
    content["server_type"] = MyForm.objects.all()
    content["list"] = server_list
    content["server_user_all"] = server_user_all
    content["business_name"] = business_name
    if len(content['list']) >0:
        content["test_error"] = True
    else:
        content["test_error"] = False
    content.update(csrf(request))

    return render_to_response('server_idc/server_type.html',content,context_instance=RequestContext(request))

