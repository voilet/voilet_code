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
import json
from django.shortcuts import render_to_response
from assets.models import  Server_Post,Poster_Source,Poster,Poster_Model,MyForm
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext



@login_required
def index(request):
    contents  = Server_Post.objects.all()
    Business = MyForm.objects.all()
    return render_to_response('server_list.html',{"contacts": contents,'title':"资产管理系统---信息列表页",'hello':'hello word!','user':request.user.first_name,"name":request.user.username,'Business':Business},context_instance=RequestContext(request))


#提交数据
class Server_From(forms.ModelForm):
    class Meta:
        model = Server_Post

@login_required
def post(req):
    if req.method == 'POST':    #验证post方法
        uf = Server_From(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            zw = uf.save()
            # zw = uf.save(commit=False)
            # s = zw.Business
            # print s
            print "保存数据"
            # return  render_to_response("1")
            return HttpResponseRedirect('/server/')
        else:
           print uf.is_valid()
    else:
        uf = Server_From()
        print "注册失败"
    Business = MyForm.objects.all()
    return render_to_response('server_post.html',{'uf':uf,'title':"添加新服务器",'hello':'hello word!','user':req.user.first_name,"name":req.user.username,'Business':Business})

'''

>>> a = MyForm.objects.get(id=1)
>>> a
<MyForm: api>
>>> b = Server_Post.objects.get(id=1)
>>> a = MyForm.objects.get(id=10)
>>> a
<MyForm: oxeye>
>>> b = Server_Post.objects.get(id=1)
>>> b.Business.add(a)

'''
#修改服务器
@login_required
def server_edit(req,id):
    edit_id = Server_Post.objects.get(id = id)
    #机房名称
    server_name = Poster.objects.all()
    #服务器型号
    server_name_id = Poster_Model.objects.all()
    #机柜位置
    Poster_Source_id = Poster_Source.objects.all()
    # print edit_id
    if req.method == 'POST':    #验证post方法
        uf = Server_From(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            uf.auto_id = edit_id.id
            zw = uf.save(commit=False)
            zw.id=edit_id.id
            zw.save()
            print "保存数据"
            return HttpResponseRedirect('/server/list_id/'+id)
        else:
            print "is over"
            print uf.is_valid()
    else:
        uf = Server_From()
        print "注册失败"
    server_id = Server_Post.objects.get(id = id)
    server_id_chem = server_id.Business.all()
    s = []

    for i in server_id_chem:
        print i.id
    # print server_id_chem
    # print
    # server_id = server_id.Business.all()
    Business = MyForm.objects.all()
    return render_to_response('server_edit.html',{'id':edit_id.id,'Business':Business,'Poster_Source_id':Poster_Source_id,'server_name_id':server_name_id,'server_name':server_name,'edit_id':edit_id,'uf':uf,'title':"添加新服务器",'hello':'hello word!','server_id':server_id_chem,'user':req.user.first_name,"name":req.user.username})

#最终页
@login_required
def list_id(req,id):
    # Business_over = Server_Post.objects.get(id = id)
    # Business_over.Business.all()
    id = Server_Post.objects.get(id = id)
    Business_over = id.Business.all()
    # Business_list = []
    # for i in Business_over:
    #     Business_list.append(i)
    # print Business_list
    Business = MyForm.objects.all()

    return render_to_response('server_over.html',{'id':id,'title':"资产管理系统---最终页",'hello':'hello word!','Business':Business,'Business_over':Business_over,'user':req.user.first_name,"name":req.user.username})



class Server_From_Poster(forms.Form):
    engine_room_name = forms.CharField()

#添加机房
@login_required
def server_add_room(req):
    Business = MyForm.objects.all()
    if req.method == 'POST':    #验证post方法
        uf = Server_From_Poster(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            engine_room_name = uf.cleaned_data['engine_room_name']
            # print engine_room_name
            name = Poster()
            name.engine_room_name = engine_room_name
            print name.save()
            print "---------------------------------------------"
            server_room_id = Poster.objects.get(engine_room_name = engine_room_name)
            #添加机房字典
            Machine_House={}
            for i in Poster.objects.all():
                Machine_House[int(i.id)]=i.engine_room_name
            save_status = {"code":1,"msg":"ok","room_id":int(server_room_id.id),"server":Machine_House}   #"Machine_House":Machine_House
            return render_to_response('server_add_room_ok.html',{'code':json.dumps(save_status),'Business':Business,'user':req.user.first_name,"name":req.user.username})
            print "保存数据"
        else:
            print uf.is_valid()
            save_status = {"code":0,"msg":"no"}
            return render_to_response('server_add_room_ok.html',{'code':save_status,'Business':Business,'user':req.user.first_name,"name":req.user.username})
    else:
        uf = Server_From_Poster()
        print "保存失败"
    Business = MyForm.objects.all()
    return render_to_response('server_add_room.html',{'room':uf,'title':"添加新服务器",'hello':'hello word!','Business':Business,'user':req.user.first_name,"name":req.user.username})





#添加机柜
class Server_Poster_Source(forms.Form):
    Poster_Source_id = forms.CharField()

@login_required
def Server_add_Poster(req):
    Business = MyForm.objects.all()
    if req.method == 'POST':    #验证post方法
        uf = Server_Poster_Source(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            Poster_Source_id = uf.cleaned_data['Poster_Source_id']
            print Poster_Source_id
            Source_name = Poster_Source()
            print Source_name
            Source_name.name = Poster_Source_id
            Source_name.save()
            print "*" * 20
            Source_json = {}
            for i in Poster_Source.objects.all():
                Source_json[int(i.id)]=i.name
            save_status = {"code":1,"msg":"ok","server":Source_json}   #"Machine_House":Machine_House
            return render_to_response('server_add_room_ok.html',{'code':json.dumps(save_status),'Business':Business,'user':req.user.first_name,"name":req.user.username})
            # print "保存数据"
        else:
            print uf.is_valid()
            save_status = {"code":0,"msg":"no"}
            return render_to_response('server_add_room_ok.html',{'code':save_status,'user':req.user.first_name,"name":req.user.username})
    else:
        uf = Server_Poster_Source()
        print "保存失败"
    Business = MyForm.objects.all()
    return render_to_response('server_add_room.html',{'room':uf,'title':"添加新服务器",'hello':'hello word!','Business':Business,'user':req.user.first_name,"name":req.user.username})



#添加机器型号
class Server_Poster_Model(forms.Form):
    Poster_Model_id = forms.CharField()

@login_required
def Server_Poster_Model_id(req):
    Business = MyForm.objects.all()
    if req.method == 'POST':    #验证post方法
        uf = Server_Poster_Model(req.POST)   #绑定POST动作
        if uf.is_valid(): #验证数据有效性
            Poster_Model_name = uf.cleaned_data['Poster_Model_id']
            print Poster_Model_name
            Source_name = Poster_Model()
            print Source_name
            Source_name.Poster_Model_name = Poster_Model_name
            Source_name.save()
            print "*" * 20
            Source_json = {}
            for i in Poster_Model.objects.all():
                Source_json[int(i.id)]=i.Poster_Model_name
            save_status = {"code":1,"msg":"ok","server":Source_json}   #"Machine_House":Machine_House
            return render_to_response('server_add_room_ok.html',{'code':json.dumps(save_status),'Business':Business,'user':req.user.first_name,"name":req.user.username})
            print "保存数据"
        else:
            print uf.is_valid()
            save_status = {"code":0,"msg":"no"}
            return render_to_response('server_add_room_ok.html',{'code':save_status,'Business':Business,'user':req.user.first_name,"name":req.user.username})
    else:
        uf = Server_Poster_Model()
        print "保存失败"
    Business = MyForm.objects.all()
    return render_to_response('server_add_room.html',{'room':uf,'title':"添加新服务器型号",'hello':'hello word!','Business':Business,'user':req.user.first_name,"name":req.user.username})


#搜索
@login_required
def search_server_ip(requst):
    emps = Server_Post.objects.all()
    id = requst.GET['search']
    Business = MyForm.objects.all()
    id = id.strip()
    # print len(id)
    if len(id) == 0:
       return render_to_response('server_search_error.html',{'emps':emps,"contacts": emps,'id':"您所查询的数据不存在",'title':"资产管理系统---搜索",'hello':'hello word!','Business':Business,'user':requst.user.first_name,"name":requst.user.username},context_instance=RequestContext(requst))
    if Server_Post.objects.filter(Server_eth2 = id):
        eth2 = Server_Post.objects.get(Server_eth2 = id)
        return render_to_response('server_over.html',{'id':eth2,'title':"资产管理系统---搜索",'hello':'hello word!','Business':Business,'user':requst.user.first_name,"name":requst.user.username})
    if Server_Post.objects.filter(Server_eth1 = id):
        eth1 = Server_Post.objects.get(Server_eth1 = id)
        return render_to_response('server_over.html',{'id':eth1,'title':"资产管理系统---搜索",'hello':'hello word!','Business':Business,'user':requst.user.first_name,"name":requst.user.username})
    if Server_Post.objects.filter(Server_Remote_control_card = id):
        control_card = Server_Post.objects.get(Server_Remote_control_card = id)
        return render_to_response('server_over.html',{'id':control_card,'title':"资产管理系统---搜索",'hello':'hello word!','Business':Business,'user':requst.user.first_name,"name":requst.user.username})
    if Server_Post.objects.filter(Server_Asset_number = id):
        number = Server_Post.objects.get(Server_Asset_number = id)
        return render_to_response('server_over.html',{'id':number,'title':"资产管理系统---搜索",'hello':'hello word!',})
    if Server_Post.objects.filter(Server_eth1__contains="id"):
    # if Server_Post.objects.filter(Q(title__icontains=id)|Q(content__icontains=id)):
        print "is ok"
        number = Server_Post.objects.get(Server_Asset_number = id)
        return render_to_response('server_over.html',{'id':number,'title':"资产管理系统---搜索",'hello':'hello word!',})
    paginator = Paginator(emps, 20)
    try:
        page = int(requst.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        voilet = paginator.page(page)
    except (EmptyPage,InvalidPage):
        voilet = paginator.page(paginator._num_pages)
    return render_to_response('server_search_error.html',{'emps':emps,"contacts": emps,'id':"您所查询的数据不存在",'title':"资产管理系统---搜索",'hello':'hello word!','Business':Business,'user':requst.user.first_name,"name":requst.user.username},context_instance=RequestContext(requst))


#按机房生成列表
@login_required
def list_room_id(req,id):
    id = Server_Post.objects.filter( Server_engine_room_id = id)
    Business = MyForm.objects.all()
    return render_to_response('server_desc.html',{'emps':id,'title':"资产管理系统---按机房显示",'hello':'hello word!','Business':Business,'user':req.user.first_name,"name":req.user.username})

#按机柜生成列表
def Location_id(req,id):
    id = Server_Post.objects.filter( Server_number_Location_id = id)
    Business = MyForm.objects.all()
    return render_to_response('server_desc.html',{'emps':id,'title':"资产管理系统--按机柜显示",'hello':'hello word!','Business':Business,'user':req.user.first_name,"name":req.user.username})



#按业务显示
@login_required
def Business(request,id):
    id = MyForm.objects.get(id = id)
    emps = id.server_post_set.all()
    paginator = Paginator(emps, 20)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        voilet = paginator.page(page)
    except (EmptyPage,InvalidPage):
        voilet = paginator.page(paginator._num_pages)
    Business = MyForm.objects.all()
    return render_to_response('server_list.html',{'emps':emps,"contacts": voilet,'title':"资产管理系统---信息列表页",'hello':'hello word!','Business':Business,'user':request.user.first_name,"name":request.user.username},context_instance=RequestContext(request))




















#测试复选柜
def test(request):
    check_box_list = request.POST.getlist('check_box_list')
    print check_box_list
    return render_to_response('test.html',{'emps':check_box_list,'title':"资产管理系统--按机柜显示",'hello':'hello word!',})


