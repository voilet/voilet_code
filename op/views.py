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
import re
from django.core.mail import send_mail
from django import forms

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from op.models import  Post,Poster_type,Poster_Source
from accounts.models import UserCreateForm
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.template import loader
from mysite.settings import  EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect




@login_required
def index(req):
    content = {}
    #emps = Post.objects.order_by('-id')
    url_path = req.get_host()
    #业务列表
    return render_to_response('op/op_add.html',content,context_instance=RequestContext(req))



class OP_From(forms.ModelForm):
    class Meta:
        model = Post

@login_required
@csrf_protect
def OP_POST(request):
    if request.method == 'POST':    #验证post方法
        #data = request.POST
        #print data
        #Occur_date = "%s %s" % (data['Occur_date_0'],data['Occur_date_1'])
        #Discovery_date = "%s %s" % (data['Discovery_date_0'],data['Discovery_date_1'])
        #Solve_date = "%s %s" % (data['Solve_date_0'],data['Solve_date_1'])
        uf = OP_From(request.POST)   #绑定POST动作
        print uf
        if uf.is_valid(): #验证数据有效性
            zw = uf.save(commit=False)
            print "*" * 100
            print zw
            zw.user_name = request.user.username
            #zw.Occur_date = Occur_date
            #zw.Discovery_date = Discovery_date
            #zw.Solve_date = Solve_date
        #zw.user_id = request.user.id
            zw.save()
            print "save ok"
        #def send_html_mail(subject, html_content, recipient_list):
        #     msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
        #     msg.content_subtype = "html" # Main content is now text/html
        #     msg.send()
        #url_path =request.get_host()
        #html_content = loader.render_to_string(
        #                'op_mail.html',            #需要渲染的html模板
        #                {'paramters':zw,'url_path':url_path}   #需要传给模板的参数
        #                )
        #send_html_mail(u'报障:' + zw.title,
        #                html_content,
        #                # ['op@funshion.com']
        #                ['songxs@funshion.com']
        #                )
        #print "发送邮件中"
            return HttpResponseRedirect('/op/')
        else:
            print "数据验证失败"
            print "error"
            # print uf
            print uf.is_valid()
    else:
        uf = OP_From()
        print "is over"
    return render_to_response('op/op_add.html',{'uf':uf},context_instance=RequestContext(request))
#查询单条记录
@login_required
def OP_select(req,id):
    op_list = Post.objects.get(id = id)
    return render_to_response('op_over.html',{'op_list':op_list,'title':"运维报障系统",'hello':'hello word!','user':req.user.first_name,"name":req.user.username})

#按用户生成列表
@login_required
def user_id(req,id):
    user_name = Post.objects.filter( user_id = id )
    return render_to_response('op_user.html',{'title':"运维报障系统－－－故障列表页",'emps':user_name,'user':req.user.first_name,"name":req.user.username})

#查询单条记录
@login_required
def OP_edit(req,id):
    edit_id = Post.objects.get(id = id)
    print "----------------------------------------------"
    # #查询 故障类型
    fault_type_id = edit_id.fault_type_id
    fault_type_id = Poster_type.objects.get(id = fault_type_id)
    # #查询报障来源
    Source_id = edit_id.Source_id
    Source_id = Poster_Source.objects.get(id = Source_id)
    if req.method == 'POST':    #验证post方法
        uf = OP_From(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            zw = uf.save(commit=False)
            zw.user_name = edit_id.user_name
            zw.user_id = edit_id.user_id
            zw.fault_type_id = fault_type_id.id
            zw.Source_id = Source_id.id
            zw.title = edit_id.title
            zw.id = edit_id.id
            zw.save()
            print "保存数据"
            return HttpResponseRedirect('/op/')
        else:
            print "数据验证失败"
            print uf.is_valid()
    else:
        print "保存数据失败----------------"
        uf = OP_From()
        print req.user.is_authenticated()
        print req.user
    return render_to_response('op_edit.html',{'user_edit':edit_id,'uf':uf,'title':"运维报障系统－－－－添加故障",'hello':'hello word!','user':req.user.first_name,"name":req.user.username})
