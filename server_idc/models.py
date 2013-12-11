#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#      History:
#=============================================================================

from django.db import models
from django.contrib.auth.models import User


class IDC(models.Model):
    name = models.CharField(max_length=64,verbose_name=u'机房名称')
    description = models.TextField()
    telphone = models.CharField(max_length=32,verbose_name=u'联系电话')
    create_time = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = verbose_name

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)

Server_System = [(i, i) for i in (u"DELL", u"HP", u"Other")]
System_os = [(i, i) for i in (u"CentOS", u"Debian")]
Cores = [(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)]
system_arch = [(i, i) for i in (u"x86_64", u"i386")]
System_usage = [(i, i) for i in (u"default", u"openstack")]



class MyForm(models.Model):
    service_name = models.CharField(max_length=30,blank=True, null=True,verbose_name=u'业务')
    service_user = models.ManyToManyField(User,blank=True, null=True,verbose_name=u'所属用户')
    description = models.TextField(blank=True, null=True,)
    def __unicode__(self):
        return self.service_name
    class Meta:
        verbose_name = u"业务管理"
        verbose_name_plural = verbose_name



class Host(models.Model):
    node_name = models.CharField(max_length=40,verbose_name=u"主机名")
    idc = models.ForeignKey(IDC,blank=True, null=True,verbose_name=u'机房')
    eth1 = models.IPAddressField(blank=True, null=True,verbose_name=u'网卡1')
    eth2 = models.IPAddressField(blank=True, null=True,verbose_name=u'网卡2')
    mac = models.CharField(max_length=20,verbose_name=u"MAC")
    internal_ip = models.IPAddressField(blank=True, null=True,verbose_name=u'远控卡')
    status = models.SmallIntegerField(blank=True, null=True,choices=SERVER_STATUS)
    brand = models.CharField(max_length=64, choices=Server_System,blank=True,null=True,verbose_name=u'硬件厂商')
    cpu = models.CharField(max_length=64,blank=True, null=True,verbose_name=u'cpu型号')
    core_num = models.SmallIntegerField(choices=Cores,blank=True, null=True,verbose_name=u'CPU核数')
    hard_disk = models.IntegerField(blank=True, null=True,verbose_name=u'硬盘')
    memory = models.IntegerField(blank=True, null=True,verbose_name=u'内存')
    system = models.CharField(u"System OS", max_length=32,choices=System_os,blank=True,null=True,)
    system_arch = models.CharField(blank=True, null=True,max_length=32, choices=system_arch)
    create_time = models.DateField(auto_now=True)
    guarantee_date = models.DateField(blank=True,null=True,verbose_name=u'保修时间')
    Cabinets = models.CharField(max_length=32,blank=True, null=True, verbose_name=u'机柜位置')
    number = models.CharField(max_length=32, blank=True, null=True,verbose_name=u'资产编号')
    editor = models.TextField(blank=True, null=True,verbose_name=u'备注')
    business = models.ManyToManyField('MyForm',blank=True, null=True,verbose_name=u'所属业务')
    usage = models.CharField(u"用途", max_length=32,choices=System_usage,)

    def __unicode__(self):
        return self.node_name

    class Meta:
        verbose_name = u"服务器"
        verbose_name_plural = verbose_name


class MaintainLog(models.Model):
    host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __unicode__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = u"维护日志"
        verbose_name_plural = verbose_name



