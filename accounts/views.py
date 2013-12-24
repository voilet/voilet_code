#!/usr/bin/python
#-*-coding:utf-8-*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from accounts.models import UserCreateForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.contrib import auth
from accounts.models import department_Mode, manager_demo

from forms import UserEditForm


@login_required
@csrf_protect
def register(request):
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
                return render_to_response('user/reg.html',content,context_instance=RequestContext(request))
        else:
            data = UserCreateForm() # UserCreationForm()
            content["data"] = data
            content.update(csrf(request))
            # return render(request, 'user/reg.html', context_instance=RequestContext(request))
            return render_to_response('user/reg.html',content,context_instance=RequestContext(request))

    return render_to_response('user/auth_error_index.html', context_instance=RequestContext(request))

#注销
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def Test_voilet(request):
    content = {}
    voilet = UserEditForm()
    content["voilet"] = voilet
    content["department"] = department_Mode.objects.all()
    content["jobs_name"] = manager_demo
    content.update(csrf(request))
    return render_to_response('user/test.html',content,context_instance=RequestContext(request))