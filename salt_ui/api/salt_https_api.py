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

import urllib2, cookielib, urllib, yaml, json
import salt_data

class salt_api_token(object):
    def __init__(self, data, url, token=None):
        self.data = data
        self.url = url
        self.headers = {
            'User-agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            "Accept" : "application/x-yaml",

        }
        self.headers.update(token)


    def run(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        req = urllib2.Request(self.url, urllib.urlencode(self.data, doseq=True), self.headers)
        req.add_header("Referer", "http://opts.jumei.com")
        resp = urllib2.urlopen(req)
        context = resp.read()
        return yaml.load(context)


class salt_api_jobs(object):
    def __init__(self, url, token=None):
        self.url = url
        self.headers = {
            'User-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            "Accept":"application/x-yaml",

        }
        self.headers.update(token)

    def run(self):
        context = urllib2.Request(self.url, headers=self.headers)
        resp = urllib2.urlopen(context)
        context = resp.read()
        return yaml.load(context)

class pxe_api(object):
    def __init__(self,data,pxe_url):
        self.data = data
        self.url = pxe_url
        self.headers = {
            'User-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        }
    def run(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
        urllib2.install_opener(opener)
        print self.data
        print self.url
        print "*" * 100
        req = urllib2.Request(self.url, urllib.urlencode(self.data), self.headers)
        req.add_header("Referer", "http://solr.int.jumei.com")
        try:
            resp = urllib2.urlopen(req)
            return_data = resp.read()
        except (urllib2.HTTPError, urllib2.URLError), e:
            return_data = e.read()
        return return_data



