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
import salt_ui.views.index
import salt_ui.log_class.api_log_class
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    #salt_ui
    url(r'(?P<id>\d+)/$',salt_ui.views.index.salt_status),
    url(r'cmd/$',salt_ui.views.index.salt_cmd),
    url(r'garins/$',salt_ui.views.index.salt_garins),
    url(r'check_install/$',salt_ui.views.index.salt_check_install),
    url(r'jinja/$',salt_ui.views.index.salt_check_jinja),
    url(r'add_node/$',salt_ui.views.index.salt_check_node),
    url(r'node_shell/$',salt_ui.views.index.salt_check_setup),
    url(r'node_server/$',salt_ui.views.index.salt_state_sls),
    url(r'logs/$',salt_ui.log_class.api_log_class.salt_data_log),
    url(r'',salt_ui.views.index.salt_index),
    #url(r'^$','salt_ui.views.index.auto'),
    #url(r'^overview$','salt_ui.views.index.overview'),
    #url(r'^minions$','salt_ui.views.index.minions'),
    #url(r'^minion$','salt_ui.views.index.minion'),
    #url(r'^execute$','salt_ui.views.index.execute'),
    #url(r'^detail$','salt_ui.views.index.detail'),
    #url(r'^getjobinfo$','salt_ui.views.index.getjobinfo'),
    #url(r'^service$','salt_ui.views.index.service'),
)


