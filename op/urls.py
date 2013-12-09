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

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    #报障
    url(r'^op/$', 'op.views.index'),
    url(r'^opadd/$', 'op.views.OP_POST'),
    #报障终级页
    url(r'^op/list/(?P<id>\d+)/$', 'op.views.OP_select'),
    #用户列表
    url(r'^op/user_list/(?P<id>\d+)/$', 'op.views.user_id'),
    #修改
    url(r'^op/user_edit/(?P<id>\d+)/$', 'op.views.OP_edit'),
    url(r'','op.views.OP_POST'),
)


