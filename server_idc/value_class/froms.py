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
from server_idc.models import IDC

class Engine_RoomForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', 'description', 'telphone']

    # def __unicode__(self, IDC, *args, **kwargs):
    #     self.idc = IDC
    #     super(Engine_RoomForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     name = self.cleaned_data.get('name')
    #     description = self.cleaned_data.get('description')
    #
    # def save(self, commit=True):
    #     """
    #     Saves the new password.
    #     """
    #     # print self.user.set_password(self.cleaned_data["newpassword"])
    #     if commit:
    #         self.idc.save()
    #     print "$" * 100
    #     return self.idc