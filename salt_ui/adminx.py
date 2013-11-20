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
from django.contrib import admin
import xadmin
from xadmin import views
from models import  AccessRecord
from django.contrib import admin
import xadmin
from salt_class_api import *
from django.template import loader,Context
from django.template.response import  TemplateResponse
from django.http import  HttpResponse

class MaintainInline(object):
    extra = 1
    style = 'accordion'


class PostAdmin(object):
    def open_detail(self,instance):
        return  "<a href='http://***/%s' target='_blank'>详情</a>" % instance.Host
    list_display = ('user_name','title','Discovery_date','Occur_date','Solve_date','Source')
    search_fields = ('title','user_name')
    exclude = ('user_name',)
    def save_models(self):
        #print dir(self)
        self.new_obj.user_name = self.request.user
        super(PostAdmin,self).save_models()






class PosterAdmin(object):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email')

class Poster_OP(object):
    list_display = ('name',)
    search_fields = ('name',)

class AccessRecordAdmin(object):
    def avg_count(self, instance):
        return int(instance.view_count / instance.user_count)
    avg_count.short_description = "Avg Count"
    avg_count.allow_tags = True
    avg_count.is_column = True

    list_display = ('test')


xadmin.site.register(AccessRecord,AccessRecordAdmin)



import yaml,json
from xadmin.views import BaseAdminView
from xadmin.views.base import filter_hook

class TestAdminView(BaseAdminView):
    def get(self, request):
        print "*" * 100
        salt_status = commands.getoutput("salt-run manage.status")
        test = yaml.load(salt_status)
        print test['up']
        return render_to_response('test.html',{'title':"django-xadmin",'contacts':test})

xadmin.site.register_view(r'test_view/$', TestAdminView, name='for_test')


#
#
#from xadmin.views.base import CommAdminView
#
#
#class AdminSettings(object):
#
#    def get_site_menu(self):
#        Article = "http://xxx.xxx"
#        Category = "http://xxx"
#        return (
#            {'title': '内容管理', 'perm': self.get_model_perm(Article, 'change'), 'menus':(
#                {'title': '游戏资料', 'icon': 'info-sign', 'url': self.get_model_url(Article, 'changelist') + '?_rel_categories__id__exact=2'},
#                {'title': '网站文章', 'icon': 'file', 'url': self.get_model_url(Article, 'changelist') + '?_rel_categories__id__exact=1'},
#            )},
#            {'title': '分类管理', 'perm': self.get_model_perm(Category, 'change'), 'menus':(
#                {'title': '主要分类', 'url': self.get_model_url(Category, 'changelist') + '?_p_parent__isnull=True'},
#                {'title': '游戏资料', 'url': self.get_model_url(Category, 'changelist') + '?_rel_parent__id__exact=2'},
#            )},
#        )
#
#xadmin.site.register(CommAdminView, AdminSettings)




















































