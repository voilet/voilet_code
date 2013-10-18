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

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    url(r'admin', include(xadmin.site.urls)),
    #url(r'^$', 'server_idc.value_class.index.Index'),
    #用户登录注册
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    (r'^accounts/login/$', 'accounts.account.user_login',),
    (r'^accounts/register/$', 'accounts.views.register'),
    (r'^accounts/loginout/$', 'accounts.views.logout_view'),
    #(r'^users/loginout/$', 'users.user_models.logout_view'),
    #salt_ui
    url(r'^$','salt_ui.views.index.auto'),
    url(r'^overview$','salt_ui.views.index.overview'),
    url(r'^minions$','salt_ui.views.index.minions'),
     url(r'^minion$','salt_ui.views.index.minion'),
    url(r'^execute$','salt_ui.views.index.execute'),
    url(r'^detail$','salt_ui.views.index.detail'),
    url(r'^getjobinfo$','salt_ui.views.index.getjobinfo'),
    url(r'^service$','salt_ui.views.index.service'),
)

