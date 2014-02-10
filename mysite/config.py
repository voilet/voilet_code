#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-14-2-10-下午9:15
#      History:
#=============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                      # Or path to database file if using sqlite3.
        'NAME': 'salt',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'voilet',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#salt api config
salt_api_url = "https://192.168.49.14/"
salt_api_user = "sa"
salt_api_pass = "centos"


#smtp

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'voilet@qq.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
#EMAIL_USE_TLS = False
