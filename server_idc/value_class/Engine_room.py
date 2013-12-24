#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2013-02-20 14:52:11
#      History:
#=============================================================================

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import commands,json,yaml
from server_idc.models import  MyForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from server_idc.value_class.froms import Engine_RoomForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User


@login_required
@csrf_protect
def Engine_Room(request):
    content = {}
    if request.method == 'POST':    #验证post方法
        uf = Engine_RoomForm(request.POST)   #绑定POST动作
        print uf
        if uf.is_valid(): #验证数据有效性
            uf.save()
            return HttpResponseRedirect("/assets/server/type/list/")
        else:
            print "save error"
            uf = Engine_RoomForm()
            content["server_type"] = MyForm.objects.all()
            content['uf'] = uf
            content.update(csrf(request))
            return render_to_response('server_idc/server_room_add.html', content, context_instance=RequestContext(request))
    else:
        uf = Engine_RoomForm()
        content['uf'] = uf
        content["user_list"]=User.objects.all()
        content["server_type"] = MyForm.objects.all()
        content.update(csrf(request))
        return render_to_response('server_idc/server_room_add.html', content, context_instance=RequestContext(request))
