#coding=UTF-8
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

from salt_ui.api import salt_api
from salt_ui.models import *
from django.contrib.auth.decorators import login_required
import commands,json,yaml
import subprocess
from salt_ui.api import *

from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


@login_required
def auto(request):
    context = {}
    context.update(csrf(request))
    services = Service.objects.all()
    context['services'] = services
    return render_to_response('index.html',context,context_instance=RequestContext(request))

#songxs add
@login_required
def salt_index(request):
    return render_to_response('saltstack/salt_index.html')

@login_required
def salt_status(request,id):
    context = {}
    id = int(id)
    if id == 1:
        master_status = commands.getoutput("salt-run manage.status")
        master_status = yaml.load(master_status)
        live = len(master_status['up'])
        if master_status['down']:
            dean = len(master_status['down'])
        else:
            dean = 0
        context['master_status']=master_status
        context['live']= live
        context['dean']= dean
        context.update(csrf(request))
        return render_to_response('saltstack/salt_status.html',context)
    if id == 2:
        proc = subprocess.Popen('salt-key', stdout=subprocess.PIPE)
        salt_key = proc.stdout.read().replace('\n','<br>')
        context["salt_key"]=salt_key
        context.update(csrf(request))
        return render_to_response('saltstack/salt_key.html',context)
    if id == 3:
        context.update(csrf(request))
        return render_to_response('saltstack/salt_cmd.html',context)

@login_required
@csrf_protect
def salt_cmd(request):
    context = {}
    if request.method == 'POST':
        salt_text = request.POST
        if salt_text['salt_cmd']:
            client = salt_api.client
            salt_cmd_lr = salt_text['salt_cmd']
            salt_cmd_lr = str(salt_cmd_lr)
            salt_cmd_context = salt_cmd_lr.partition("@")
            salt_cmd_context = list(salt_cmd_context)
            salt_cmd_len = salt_cmd_lr.split("@")
            if len(salt_cmd_len) >1 :
                cmd = client.cmd( salt_cmd_context[0], 'cmd.run', [salt_cmd_context[2:]] )
                context["cmd_run"]=cmd
                context["cmd_Advanced"]=False
                context["salt_cmd"]=salt_text['salt_cmd']
                context.update(csrf(request))
                return render_to_response('saltstack/salt_cmd_run.html',context)
            else:
                cmd = client.cmd("*", 'cmd.run', [salt_text['salt_cmd']])
                context["cmd_run"]=cmd
                context["cmd_Advanced"]=True
                context["salt_cmd"]=salt_text['salt_cmd']
                context.update(csrf(request))
                return render_to_response('saltstack/salt_cmd_run.html',context)
        else:
            return render_to_response('saltstack/salt_cmd_run.html',context)

@login_required
@csrf_protect
def salt_garins(request):
    context = {}
    if request.method == 'POST':
        salt_text = request.POST
        if salt_text['salt_cmd']:
            client = salt_api.client
            salt_cmd_lr = salt_text['salt_cmd']
            salt_cmd_context = salt_cmd_lr.partition("@")
            salt_cmd_context = list(salt_cmd_context)
            salt_cmd_len = salt_cmd_lr.split("@")
            if len(salt_cmd_len) >1 :
                cmd = client.cmd( salt_cmd_context[0], 'grains.item', [salt_cmd_context[2]] )
                context["cmd_run"]=cmd
                context["cmd_Advanced"]=False
                context["salt_cmd"]=salt_text['salt_cmd']
                context.update(csrf(request))
                return render_to_response('saltstack/salt_cmd_grains_run.html',context)
            else:
                cmd = client.cmd(salt_text['salt_cmd'].strip(), 'grains.items')
                context['cmd_run'] = cmd
                context["cmd_Advanced"]=True
                context['salt_cmd'] = salt_text['salt_cmd']
                context.update(csrf(request))
                return render_to_response('saltstack/salt_cmd_grains_run.html',context)
        else:
            return render_to_response('saltstack/salt_cmd_grains_run.html',context)
    else:
        context.update(csrf(request))
        return render_to_response('saltstack/salt_garins.html',context)

#自动化部署
@login_required
@csrf_protect
def salt_nginx(request):
     context = {}
     return render_to_response('saltstack/salt_cmd_run.html',context)

#系统初始化
@login_required
@csrf_protect
def salt_check_install(request):
     context = {}
     if request.method == 'POST':
        salt_text = request.POST
        return render_to_response('saltstack/salt_check_install.html',context)
     else:
         server_list = open("/srv/salt/check_install/hostname.jinja","r")
         server = server_list.read()
         server_list.close()
         server_node = open("/etc/salt/roster","r")
         node = server_node.read()
         server_node.close()
         context["server"] = server
         context["node"] = node
         context["cmd_Advanced"]=True
         context.update(csrf(request))
         return render_to_response('saltstack/salt_check_install.html',context)

#jinja
@login_required
@csrf_protect
def salt_check_jinja(request):
     context = {}
     if request.method == 'POST':
        salt_text = request.POST
        context.update(csrf(request))
        server_list = open("/srv/salt/check_install/hostname.jinja","w")
        server_list.write(salt_text['salt_content_jinja'])
        server_list.close()
        return render_to_response('saltstack/salt_check_install.html',context)



#jinja
@login_required
@csrf_protect
def salt_check_node(request):
     context = {}
     if request.method == 'POST':
        salt_text = request.POST
        context.update(csrf(request))
        server_list = open("/etc/salt/roster","w")
        server_list.write(salt_text['salt_content_node'])
        server_list.close()
        context["salt_node"] = True
        return render_to_response('saltstack/salt_check_install.html',context)