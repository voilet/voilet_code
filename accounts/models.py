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

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True,)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',  )

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit)
        # user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user

manager_demo = [(i, i) for i in (u"经理", u"主管", u"负责人",u"管理员",u"BOOS")]

class ProfileBase(type):                    #对于传统类，他们的元类都是types.ClassType
    def __new__(cls,name,bases,attrs):      #带参数的构造器，__new__一般用于设置不变数据类型的子类
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

class ProfileUser(object):
    __metaclass__ = ProfileBase     #类属性

class MyProfile(ProfileUser):
    department = models.CharField(max_length=60, blank=True, verbose_name=u"部门")      #真实姓名
    jobs = models.CharField(max_length = 20,choices=manager_demo, blank=True,verbose_name=u"职位")              #级别

    def __unicode__(self):
        return self.department
    class Meta:
        verbose_name = u"新增字段"
        verbose_name_plural = verbose_name