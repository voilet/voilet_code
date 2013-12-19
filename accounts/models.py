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

