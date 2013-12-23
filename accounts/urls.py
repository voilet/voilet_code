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
import accounts.views
import accounts.account
import accounts.user_mode.user_edit_class
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    #user
    # url(r'(?P<id>\d+)/$',salt_ui.views.index.salt_status),
    (r'^login/$', accounts.account.user_login),
    (r'^edit_passwd/$', accounts.account.change_password),
    (r'^adduser/$', accounts.views.register),
    (r'^user_edit/(?P<id>\d+)/$', accounts.user_mode.user_edit_class.user_edit),
    (r'^user_list/$', accounts.user_mode.user_edit_class.user_list),
    (r'^add_department/$', accounts.user_mode.user_edit_class.department_add),
    (r'^list_department/$', accounts.user_mode.user_edit_class.department_list),
    (r'^loginout/$', accounts.views.logout_view),
    # url(r'logs/$',salt_ui.log_class.api_log_class.salt_data_log),
)


