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
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from accounts.models import UserCreateForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

import time


class user_from(forms.ModelForm):
    # FAVORITE_COLORS_CHOICES = MyForm.objects.values_list("id","service_name")
    # business = forms.MultipleChoiceField(required=False,
    #     widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    class Meta:
        model = User
@login_required
@csrf_protect
def register(request):
    content = {}
    data_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if request.method == 'POST':
        uf = user_from(request.POST)
        password = request.POST.getlist("password")
        # mac = request.POST.getlist("mac")
        if uf.is_valid():
            zw = uf.save(commit=False)
            zw.password = make_password(password)
            zw.last_login = data_time
            zw.date_joined = data_time
            zw.is_staff = 1
            zw.save()
            # form.is_staff = 1
            # new_user = form.save(commit=False)
            # new_user.is_staff = 1
            # new_user.save()
            return HttpResponseRedirect('/salt/')
        else:
            print "error"
            content["form"] = user_from()
            content.update(csrf(request))
            return render_to_response('user/register.html',content,context_instance=RequestContext(request))
    else:
        content["form"] = user_from()
        content["data_time"] = data_time
        content.update(csrf(request))
        return render_to_response('user/register.html',content,context_instance=RequestContext(request))