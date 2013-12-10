#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================


import json

s = {'java-15': 'eth0      Link encap:Ethernet  HWaddr FA:16:3E:41:0B:BA  \n          inet addr:192.168.49.15  Bcast:192.168.49.255  Mask:255.255.255.0\n          inet6 addr: fe80::f816:3eff:fe41:bba/64 Scope:Link\n          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n          RX packets:193156 errors:0 dropped:191 overruns:0 frame:0\n          TX packets:56495 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:1000 \n          RX bytes:47426122 (45.2 MiB)  TX bytes:6330407 (6.0 MiB)\n          Interrupt:11 Base address:0x8000 \n\nlo        Link encap:Local Loopback  \n          inet addr:127.0.0.1  Mask:255.0.0.0\n          inet6 addr: ::1/128 Scope:Host\n          UP LOOPBACK RUNNING  MTU:16436  Metric:1\n          RX packets:0 errors:0 dropped:0 overruns:0 frame:0\n          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:0 \n          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)', 'recommend-tomcat-52': 'eth0      Link encap:Ethernet  HWaddr fa:16:3e:5d:15:1c  \n          inet addr:192.168.49.52  Bcast:192.168.49.255  Mask:255.255.255.0\n          inet6 addr: fe80::f816:3eff:fe5d:151c/64 Scope:Link\n          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n          RX packets:4169879 errors:0 dropped:91 overruns:0 frame:0\n          TX packets:3250020 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:1000 \n          RX bytes:916378415 (873.9 MiB)  TX bytes:277512947 (264.6 MiB)\n          Interrupt:11 Base address:0x2000 \n\nlo        Link encap:Local Loopback  \n          inet addr:127.0.0.1  Mask:255.0.0.0\n          inet6 addr: ::1/128 Scope:Host\n          UP LOOPBACK RUNNING  MTU:16436  Metric:1\n          RX packets:1008 errors:0 dropped:0 overruns:0 frame:0\n          TX packets:1008 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:0 \n          RX bytes:169196 (165.2 KiB)  TX bytes:169196 (165.2 KiB)'}
print s["java-15"]