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


@login_required
def index(request):
    title = 'Toolkits &middot; 管理 - 首页'
    return render_to_response('main.html', locals(), context_instance=RequestContext(request))

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST) # UserCreationForm(request.POST)
        if form.is_valid():
            # form.is_staff = 1
            new_user = form.save(commit=False)
            new_user.is_staff = 1
            new_user.save()
            # perhaps set permissions of the new user
            # return render(request, 'registration/success.html') # need to create success.html
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm() # UserCreationForm()
    return render(request, 'user/register.html', {'form':form})

#注销
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")