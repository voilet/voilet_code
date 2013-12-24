#!/usr/bin/python
#-*-coding:utf-8-*-

from django import forms
from fields import UsernameField,PasswordField
from django.contrib.auth import authenticate,login
from accounts.models import User

class LoginForm(forms.Form):
    username = UsernameField(required=True, max_length=12, min_length=4)
    password = PasswordField(required=True, max_length=12, min_length=6)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u"您输入的用户名或密码不正确!")
            elif not self.user_cache.is_active or not self.user_cache.is_staff:
                raise forms.ValidationError(u"您输入的用户名或密码不正确!")
            else:
                login(self.request, self.user_cache)
        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class ChangePasswordForm(forms.Form):
    """
        A form used to change the password of a user in the admin interface.
    """
    newpassword = PasswordField(required=True, max_length=12, min_length=6)
    renewpassword = PasswordField(required=True, max_length=12, min_length=6)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        newpassword = self.cleaned_data.get('newpassword')
        renewpassword = self.cleaned_data.get('renewpassword')
        if newpassword and renewpassword:
            if newpassword != renewpassword:
                raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        return renewpassword

    def save(self, commit=True):
        """
        Saves the new password.
        """
        # print self.user.set_password(self.cleaned_data["newpassword"])
        if commit:
            self.user.save()
        return self.user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'department', 'jobs']
