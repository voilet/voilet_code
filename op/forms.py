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
# from op.models import  Post,Poster,Poster_type,Poster_Source
from django.contrib.admin import widgets
#
# class UserName(forms.ModelForm):
#     class Meta:
#         model = Post

date = forms.DateTimeField(widget=widgets.AdminDateWidget(), label=u'时间')

class OpPost(forms.ModelForm):
    class Meta:
        mode = Post
    def save(self, commit=True):
        s = "sadfasf"
