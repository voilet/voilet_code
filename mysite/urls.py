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
import salt_ui.urls
import op.urls
import server_idc.urls
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    url(r'admin/', include(xadmin.site.urls)),
    # url(r'^voilet/test/$', 'server_idc.value_class.index.Index'),
    #用户登录注册
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    (r'^accounts/login/$', 'accounts.account.user_login',),
    (r'^accounts/register/$', 'accounts.views.register'),
    (r'^accounts/loginout/$', 'accounts.views.logout_view'),
    url(r'^$', 'salt_ui.views.index.salt_index'),

    #搜索
    # url(r'^search/$', 'assets.views.search'),
    #编缉器
    url(r'^ueditor_imgup$','ueditor.Ueditor.views.ueditor_ImgUp',),
    url(r'^ueditor_fileup$','ueditor.Ueditor.views.ueditor_FileUp'),
    url(r'^ueditor_getRemoteImage$','ueditor.Ueditor.views.ueditor_getRemoteImage'),
    url(r'^ueditor_scrawlUp$','ueditor.Ueditor.views.ueditor_ScrawUp'),
    url(r'^ueditor_getMovie$','ueditor.Ueditor.views.ueditor_getMovie'),
    url(r'^ueditor_imageManager$','ueditor.Ueditor.views.ueditor_imageManager'),
    #报障
    url(r'op/', include(op.urls)),
    #salt_ui
    url(r'salt/', include(salt_ui.urls)),
     #资产管理
    url(r'assets/', include(server_idc.urls)),
    #url(r'',include(salt_ui.urls)),
)

