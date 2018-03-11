# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/11 12:48

"""
第11章 网络与Web编程
"""

"""
11.1 作为客户端与HTTP交互
"""
from urllib import request

# request.urlopen()
# 简单的实现GET,POST等
# 如果需要更加复杂的交互使用第三方库 requests
# 如果不希望使用第三方库 requests，还可以使用底层的http.client
from http.client import HTTPConnection
from urllib import parse

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()

print('Status', resp.status)
for n, v in resp.getheaders():
    print(n, v)

"""
11.2 创建TCP服务器
"""