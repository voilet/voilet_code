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
from django.contrib.auth.hashers import make_password
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from accounts.models import *
from accounts.forms import UserEditForm
import time,json

class edit_user_from(forms.ModelForm):
    class Meta:
        model = User

@login_required
@csrf_protect
def user_list(request):
    content = {}
    if request.user.is_superuser:
        user_list = User.objects.all()
        for i in user_list:
            username = i.username
            # test = username.MyProfile_set.all()
            # print test

        content["user_list"] = user_list
        content.update(csrf(request))
        return render_to_response('user/user_list.html',content,context_instance=RequestContext(request))
    else:
        return render_to_response('user/auth_error_index.html', context_instance=RequestContext(request))

@login_required
@csrf_protect
def user_edit(request, id):
    voilet_list = User.objects.get(id=id)
    content = {}
    data_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if request.user.is_superuser:
        if request.method == 'POST':
            if request.POST.getlist("password1") == request.POST.getlist("password2"):
                uf = UserEditForm(request.POST)
                if uf.is_valid():
                    voilet_list.department = uf.instance.department
                    voilet_list.jobs = uf.instance.jobs
                    voilet_list.first_name = uf.instance.first_name
                    voilet_list.save()
                    return HttpResponseRedirect('/accounts/user/' + id + '/')
                else:
                    print "is over"
        else:
            content["userall"] = UserEditForm()
            content["user_list"] = voilet_list
            content["department"] = department_Mode.objects.all()
            content["jobs_name"] = manager_demo
            content.update(csrf(request))
            return render_to_response('user/user_edit.html',content,context_instance=RequestContext(request))
    else:
        return render_to_response('user/auth_error_index.html', context_instance=RequestContext(request))

@login_required
@csrf_protect
def user_id(request, id):
    voilet_list = User.objects.get(id=id)
    content = {}
    data_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if request.method == 'POST':
        if request.POST.getlist("password1") == request.POST.getlist("password2"):
            uf = edit_user_from(request.POST)
            if uf.is_valid():
                print "is ok"
                zw = uf.save(commit=False)
                zw.last_login = data_time
                zw.date_joined = data_time
                zw.id = id
                zw.password = make_password(request.POST.getlist("password1"))
                zw.save()
                content["user_list"] = voilet_list
                content.update(csrf(request))
                return render_to_response('user/user_edit.html',content,context_instance=RequestContext(request))
            else:
                print "is over"
    else:
        content["data_time"] = data_time
        content["user_list"] = voilet_list
        content["department"] = department_Mode.objects.all()
        content["jobs_name"] = manager_demo
        content.update(csrf(request))
        return render_to_response('user/user_page.html',content,context_instance=RequestContext(request))

class department_from(forms.ModelForm):
    class Meta:
        model = department_Mode

@login_required
@csrf_protect
def department_add(request):
    content = {}
    if request.user.is_superuser:
        uf = department_from(request.POST)
        if request.method == 'POST':
            if uf.is_valid():
                uf.save()
                return HttpResponseRedirect('/accounts/list_department/')
            else:
                department_list = department_from()
                content["department_list"] = department_list
                content.update(csrf(request))
                return render_to_response('user/department_add.html',content, context_instance=RequestContext(request))
        else:
            department_list = department_from()
            content["department_list"] = department_list
            content.update(csrf(request))
            return render_to_response('user/department_add.html',content, context_instance=RequestContext(request))
    else:
        return render_to_response('user/auth_error_index.html', context_instance=RequestContext(request))

@login_required
@csrf_protect
def department_list(request):
    content = {}
    if request.user.is_superuser:
        if request.method == 'POST':
            print u"注册数据"
            form = UserCreateForm(request.POST) # UserCreationForm(request.POST)
            print u"验证完成"
            if form.is_valid():
                # form.is_staff = 1
                new_user = form.save(commit=False)
                new_user.is_staff = 1
                new_user.save()
                # perhaps set permissions of the new user
                # return render(request, 'registration/success.html') # need to create success.html
                return HttpResponseRedirect('/')
            else:
                content["form"] = form
                content.update(csrf(request))
                return render_to_response('user/department_list.html',content,context_instance=RequestContext(request))
        else:
            department_list = department_Mode.objects.all()
            content["department_list"] = department_list
            content.update(csrf(request))
            return render_to_response('user/department_list.html',content,context_instance=RequestContext(request))
    else:
        return render_to_response('user/auth_error_index.html', context_instance=RequestContext(request))