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

import ConfigParser
def salt_conf():
    cfg=ConfigParser.ConfigParser()
    cfg.read("config.ini")
    salt_url=cfg.get('salt_api','url')
    salt_user = cfg.get("salt_user",'user')
    salt_pass = cfg.get("salt_user","password")
    return salt_url,salt_user,salt_pass
