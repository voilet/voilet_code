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
from server_idc.models import service_log

class IDClog_From(forms.ModelForm):
    class Meta:
        model = service_log

def idc_log(edit_user_name, edit_server_nodename, edit_server_type, old_editname, old_editdatetime):
    idc_edit_logs = service_log(user_name=edit_user_name, edit_server_nodename=edit_server_nodename, edit_server_type=edit_server_type, old_editname=old_editname, old_editdatetime=old_editdatetime,)
    idc_edit_logs.save()
