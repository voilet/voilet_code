#!/usr/bin/python
#-*-coding:utf-8-*-

import re
from django.core.validators import RegexValidator

username_re = re.compile(r'^([\w]{9}|[a-zA-Z]{1}[\w]+?)$')
username = RegexValidator(username_re, '学生:您的学号,管理员:4-12位,由字母数字下划线组成,首字母为字母', 'invalid')

password_re = re.compile(r'^[\w]+?$')
password = RegexValidator(password_re, '密码由字母数字下划线组成的字符串，最少为6位', 'invalid')