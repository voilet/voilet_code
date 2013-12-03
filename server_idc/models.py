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


class IDC(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    contact = models.CharField(max_length=32)
    telphone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    customer_id = models.CharField(max_length=128)

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


class service_types(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"业务类型"
        verbose_name_plural = verbose_name

class MyForm(models.Model):
    check = models.CharField(max_length=30,blank=True, null=True,verbose_name=u'业务')
    def __unicode__(self):
        return self.check
    class Meta:
        verbose_name = u"业务管理"


class Host(models.Model):
    node_name = models.CharField(max_length=40,verbose_name=u"主机名")
    idc = models.ForeignKey(IDC,verbose_name=u'机房')
    ip = models.IPAddressField(blank=True, null=True)
    internal_ip = models.IPAddressField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True,choices=SERVER_STATUS)
    brand = models.CharField(max_length=64, choices=Server_System,verbose_name=u'服务器型号')
    cpu = models.CharField(max_length=64,verbose_name=u'cpu型号')
    core_num = models.SmallIntegerField(choices=Cores,verbose_name=u'CPU核数')
    hard_disk = models.IntegerField(verbose_name=u'硬盘')
    memory = models.IntegerField(verbose_name=u'内存')
    system = models.CharField(u"System OS", max_length=32,choices=System_os)
    system_arch = models.CharField(max_length=32, choices=system_arch)
    create_time = models.DateField(blank=True, null=True,verbose_name=u'创建时间')
    guarantee_date = models.DateField(blank=True, null=True,verbose_name=u'保修时间')
    #service_type = models.ForeignKey(service_types,verbose_name=u'业务')
    Cabinets = models.CharField(max_length=32,blank=True, null=True, verbose_name=u'机柜位置')
    number = models.CharField(max_length=32, blank=True, null=True,verbose_name=u'资产编号')
    editor = models.TextField(blank=True, null=True,verbose_name=u'备注')
    business = models.ManyToManyField('MyForm',blank=True, null=True,verbose_name=u'所属业务')

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



