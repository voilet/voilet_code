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


from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from salt_ui.models import *
from server_idc.models import service_log,MyForm

class IDClog_From(forms.ModelForm):
    class Meta:
        model = service_log

def idc_log(edit_user_name, edit_server_nodename, edit_server_type, old_editname, old_editdatetime, edit_server_id, edit_user_id):
    idc_edit_logs = service_log(edit_user_name=edit_user_name, edit_server_nodename=edit_server_nodename, edit_server_type=edit_server_type, old_editname=old_editname, old_editdatetime=old_editdatetime, edit_server_id=edit_server_id, edit_user_id=edit_user_id)
    idc_edit_logs.save()

def server_log_list(request):
    context = {}
    log_list = service_log.objects.all().order_by("-id")
    context["log"] = log_list
    context["server_type"] = MyForm.objects.all()
    context.update(csrf(request))
    return render_to_response('server_idc/log.html',context,context_instance=RequestContext(request))