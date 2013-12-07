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
from salt_https_api import salt_api_token
#from salt_data import salt_conf
##import salt_data
#
#salt_conf()

def token_id():
    s = salt_api_token(
        {
        "username":"sa",
        "password":"centos",
        "eauth":"pam"
                       },
        "https://192.168.49.14/login",
        {}
    )
    test = s.run()
    salt_token = [i["token"] for i in test["return"]]
    salt_token = salt_token[0]
    return salt_token

