#!/usr/bin/python
#-*-coding:utf-8-*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from forms import LoginForm, ChangePasswordForm
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        # print form
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            return render_to_response('user/login.html', {"form": form},RequestContext(request))
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
    return render_to_response('user/login.html', RequestContext(request))


@login_required
def change_password(request):
    if request.method == "POST":
        # print request.POST
        form = ChangePasswordForm(user=request.user, data=request.POST)
        # print form.is_valid()
        if form.is_valid():
            form.save()
            ret = {"status": 1, "msg": "is ok"}
        else:
            ret = {"status": 0, "msg": "is over"}
        obj = json.dumps(ret)
        return HttpResponse(obj)
    else:
        obj = json.dumps({"status": -1, "msg": "error"})
        return HttpResponse(obj)
