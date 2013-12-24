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
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import datetime
# from accounts.models import ProfileBase


manager_demo = [(i, i) for i in (u"经理", u"主管", u"项目责任人", u"管理员", u"BOOS")]


class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
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

class Profile(object):
    __metaclass__ = ProfileBase

class DepartmentGroup(models.Model):
    department_groups_name = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'组名')
    description = models.TextField(verbose_name=u"介绍",blank=True, null=True,)

    def __unicode__(self):
        return self.department_groups_name

    class Meta:
        verbose_name = u"部门组"
        verbose_name_plural = verbose_name

class department_Mode(models.Model):
    department_name = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'部门名称')
    # dt_group = models.ForeignKey(DepartmentGroup, blank=True, null=True, verbose_name=u"部门组")
    description = models.TextField(verbose_name=u"介绍", blank=True, null=True,)

    def __unicode__(self):
        return self.department_name

    class Meta:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name


class MyProfile(Profile):
    department = models.ForeignKey(department_Mode, max_length=60, blank=True, null=True, verbose_name=u"部门")
    jobs = models.CharField(max_length=20, choices=manager_demo, blank=True, null=True, verbose_name=u"职位")

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name = u"新增字段"
        verbose_name_plural = verbose_name

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    department = forms.ModelChoiceField(queryset=department_Mode.objects.all(), empty_label=u"请选择部门")
    jobs = models.CharField(max_length=20, choices=manager_demo, blank=True, null=True, verbose_name=u"职位")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', 'department', 'jobs')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit)
        user.first_name = self.cleaned_data["first_name"]
        user.department = self.cleaned_data["department"]
        user.jobs = self.cleaned_data["jobs"]
        user.is_staff = 1
        if commit:
            user.save()
        return user








