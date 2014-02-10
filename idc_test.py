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

import requests
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
import multiprocessing
import urllib2, time, requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
        'http://www.python.org',
        'http://www.python.org/about/',
        'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
        'http://www.python.org/doc/',
        'http://www.python.org/download/',
        'http://www.python.org/getit/',
        'http://www.python.org/community/',
        'https://wiki.python.org/moin/',
        'http://planet.python.org/',
        'https://wiki.python.org/moin/LocalUserGroups',
        'http://www.python.org/psf/',
        'http://docs.python.org/devguide/',
        'http://www.python.org/community/awards/'
        # etc..
        ]

LIST = {
    ##############################
    #监控广告AD/ADM
    (
        'http://ad.funshion.com/control/adredirect.html',
        'http://ad.funshion.com/control/ad_define.fai',
        'http://ad.funshion.com/pause/?c=shy,,',
        'http://adm.funshion.com/ad/2010-12/19CA07D0_07AE_9F44_52D2_481FAB1722F4.swf',
        ):[
        #UNICOM HAPROXY
        '60.31.184.9',      #hu he hao te
        '119.188.26.90',    #ji nan
        '202.110.64.250',   #zheng zhou
        '61.55.190.225',    #shi jia zhuang
        '125.211.218.158',  #ha er bin
        '125.211.218.151',
        '124.95.136.6',     #shen yang
        '124.95.136.11',
        '221.204.189.29',   #tai yuan
        '221.204.189.30',   #tai yuan
        #TELECOM HAPROXY
        '59.53.56.55',      #nan chang
        '116.252.181.190',  #nan ning
        '113.17.170.222',  #nan ning
        '222.211.83.92',    #cheng du
        '222.211.83.93',
        '117.27.153.29',    #fuzhou
        '117.27.153.30',
        '61.147.117.29',    #yangzhou
        '61.147.117.30',
        #'119.97.178.30',    #wu han
        '122.224.176.30',   #hang zhou
        '119.84.71.30',     #chong qing
        '121.12.171.30',    #dong guan
        '117.34.68.90',     #xi'an
        #YIDONG
        '111.1.46.224',     #zhejiang
        '183.203.15.22',    #shan xi
        '183.203.15.23',
        ],

    ##############################
    #监控网站外围SQUID
    #DYNAMIC group
    (
        'http://api.funshion.com/embed_zone',
        'http://i.funshion.com',
        'http://update.funshion.com/update/check.php?s=001D7D3F57DF&id=0&v=2.3.0.25&xml=true',
        ):[
        #UNICOM HAPROXY
        '60.31.184.9',      #hu he hao te
        '119.188.26.90',    #ji nan
        '202.110.64.250',   #zheng zhou
        '61.55.190.225',    #shi jia zhuang
        '125.211.218.158',  #ha er bin
        '125.211.218.151',
        '124.95.136.6',     #shen yang
        '124.95.136.11',
        '221.204.189.29',   #tai yuan
        '221.204.189.30',   #tai yuan
        #TELECOM HAPROXY
        '59.53.56.55',      #nan chang
        '116.252.181.190',  #nan ning
        '113.17.170.222',  #nan ning
        '222.211.83.92',    #cheng du
        '222.211.83.93',
        '117.27.153.29',    #fuzhou
        '117.27.153.30',
        '61.147.117.29',    #yangzhou
        '61.147.117.30',
        #'119.97.178.30',    #wu han
        '122.224.176.30',   #hang zhou
        '119.84.71.30',     #chong qing
        '121.12.171.30',    #dong guan
        '117.34.68.90',     #xi'an
        #YIDONG
        '111.1.46.224',     #zhejiang
        '183.203.15.22',    #shan xi
        '183.203.15.23',
        ],

    #FS group
    (
        'http://fs.funshion.com/publish/first?ver=5',
        'http://www.funshion.com',
        ):[
        #UNICOM HAPROXY
        '60.31.184.9',      #hu he hao te
        '119.188.26.90',    #ji nan
        '202.110.64.250',   #zheng zhou
        '61.55.190.225',    #shi jia zhuang
        '125.211.218.158',  #ha er bin
        '125.211.218.151',
        '124.95.136.6',     #shen yang
        '124.95.136.11',
        '221.204.189.29',   #tai yuan
        '221.204.189.30',   #tai yuan
        #TELECOM HAPROXY
        '59.53.56.55',      #nan chang
        '116.252.181.190',  #nan ning
        '113.17.170.222',  #nan ning
        '222.211.83.92',    #cheng du
        '222.211.83.93',
        '117.27.153.29',    #fuzhou
        '117.27.153.30',
        '61.147.117.29',    #yangzhou
        '61.147.117.30',
        #'119.97.178.30',    #wu han
        '122.224.176.30',   #hang zhou
        '119.84.71.30',     #chong qing
        '121.12.171.30',    #dong guan
        '117.34.68.90',     #xi'an
        #YIDONG
        '111.1.46.224',     #zhejiang
        '183.203.15.22',    #shan xi
        '183.203.15.23',
        ],

    #STATIC group
    (
        'http://static.funshion.com/css/default.css',
        'http://www.btstream.org/fsp/2011-05-17/23811438_1305626014_282.fsp',
        'http://q.funshion.com/api/torrents/95837/189b92098ca76ac/f6bcf9b74b7a5e6fba067b34035c7dfb240036fd',
        'http://q.funshion.com/v5/getfsp/94209?h=1'
        'http://vas.funshion.com/css/default.css',
        'http://jsonfe.funshion.com/list/?cli=iphone&ver=1.1.0.1&pagesize=20&type=movie&page=20'
        'http://push.funshion.com/api/reset_badge.php?devicetoken=(null)'
        ):[
        #UNICOM HAPROXY
        '60.31.184.9',      #hu he hao te
        '119.188.26.90',    #ji nan
        '202.110.64.250',   #zheng zhou
        '61.55.190.225',    #shi jia zhuang
        '125.211.218.158',  #ha er bin
        '125.211.218.151',
        '124.95.136.6',     #shen yang
        '124.95.136.11',
        '221.204.189.29',   #tai yuan
        '221.204.189.30',   #tai yuan
        #TELECOM HAPROXY
        '59.53.56.55',      #nan chang
        '116.252.181.190',  #nan ning
        '113.17.170.222',  #nan ning
        '222.211.83.92',    #cheng du
        '222.211.83.93',
        '117.27.153.29',    #fuzhou
        '117.27.153.30',
        '61.147.117.29',    #yangzhou
        '61.147.117.30',
        #'119.97.178.30',    #wu han
        '122.224.176.30',   #hang zhou
        '119.84.71.30',     #chong qing
        '121.12.171.30',    #dong guan
        '117.34.68.90',     #xi'an
        #YIDONG
        '111.1.46.224',     #zhejiang
        '183.203.15.22',    #shan xi
        '183.203.15.23',
        ],

    #IMG group
    (
        'http://img.funshion.com/attachment/images/2008/08-04/5372255_1217833540_699_m.jpg',
        'http://img1.funshion.com/attachment/images/2008/08-04/5372255_1217833540_699_m.jpg',
        'http://www.th123.com',
        ):[
        #UNICOM HAPROXY
        '60.31.184.9',      #hu he hao te
        '119.188.26.90',    #ji nan
        '202.110.64.250',   #zheng zhou
        '61.55.190.225',    #shi jia zhuang
        '125.211.218.158',  #ha er bin
        '125.211.218.151',
        '124.95.136.6',     #shen yang
        '124.95.136.11',
        '221.204.189.29',   #tai yuan
        '221.204.189.30',   #tai yuan
        #TELECOM HAPROXY
        '59.53.56.55',      #nan chang
        '116.252.181.190',  #nan ning
        '113.17.170.222',  #nan ning
        '222.211.83.92',    #cheng du
        '222.211.83.93',
        '117.27.153.29',    #fuzhou
        '117.27.153.30',
        '61.147.117.29',    #yangzhou
        '61.147.117.30',
        #'119.97.178.30',    #wu han
        '122.224.176.30',   #hang zhou
        '119.84.71.30',     #chong qing
        '121.12.171.30',    #dong guan
        '117.34.68.90',     #xi'an
        #YIDONG
        '111.1.46.224',     #zhejiang
        '183.203.15.22',    #shan xi
        '183.203.15.23',
        ]

    }





def func():
   for i in LIST.keys():
       time.sleep(5)
       print LIST[i]

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)
    # result = []
    # for i in LIST.keys():
    #     IP_list = i
    #     result.append(pool.apply_async(func, (IP_list,)))
    pool.apply_async(func)

    pool.close()
    pool.join()
    print "Sub-process(es) done."

# start = time.time()
# pool = ThreadPool(8)
# results = pool.map(urllib2.urlopen, urls)
# pool.close()
# pool.join()
# end = time.time()
# print("Time used:", end-start)

