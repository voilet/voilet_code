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
# import xadmin
#import op.views
# xadmin.autodiscover()

urlpatterns = patterns('',
    #资产管理
    url(r'edit_id/(?P<id>\d+)/$', 'server_idc.value_class.index.server_edit'),
    url(r'update_id/(?P<id>\d+)/$', 'server_idc.value_class.service_update.server_update'),
    url(r'server_type/(?P<id>\d+)/$', 'server_idc.value_class.index.server_type_list'),
    url(r'serverid/list/(?P<id>\d+)/$', 'server_idc.value_class.index.services_list_id'),
    url(r'server/type/add/', 'server_idc.value_class.index.server_type_add'),
    url(r'server/type/list/', 'server_idc.value_class.index.auth_server_type_list'),
    url(r'server/type/del/', 'server_idc.value_class.index.auth_server_type_delete'),
    url(r'server/list/', 'server_idc.value_class.index.services_list_all'),
    url(r'server/add/', 'server_idc.value_class.index.Index_add'),

    # url(r'/', 'server_idc.value_class.index.services_list_all'),

)


