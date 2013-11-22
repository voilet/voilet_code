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
        return render_to_response('saltstack/salt_status.html',context)
    if id == 2:
        proc = subprocess.Popen('salt-key', stdout=subprocess.PIPE)
        salt_key = proc.stdout.read().replace('\n','<br>')
        context["salt_key"]=salt_key
        return render_to_response('saltstack/salt_key.html',context)
    if id == 3:
        return render_to_response('saltstack/salt_cmd.html',context)
    if request.method == 'POST':
        client = salt_api.client
        cmd = client.cmd('*', 'cmd.run', ['ls -l'])
        context["cmd_run"]=cmd
        print context
        return render_to_response('saltstack/salt_cmd_run.html',context)
        #grains = client.cmd(target, 'grains.items')
