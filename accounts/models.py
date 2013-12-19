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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import xadmin

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

#==================扩展用户====================================
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    major = models.CharField(max_length=100,default='', blank=True,verbose_name="扩展字段1")
    address = models.CharField(max_length=200,default='',blank=True,verbose_name="地址")

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = u"扩展字段"
        verbose_name_plural = verbose_name

def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
#==================扩展用户结束================================



"""用户模块扩展"""
class ProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
"""用户模块扩展"""