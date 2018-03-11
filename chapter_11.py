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

"""
11.3 创建UDP服务器
"""

"""
11.4 通过CIDR地址生成对应的IP地址集
"""
# ipaddress模块

"""
11.5 创建一个简单的REST接口
"""

"""
11.6 通过XML-RPC实现简单的远程调用
"""

"""
11.7 在不同的Python解释器之间交互
"""

"""
11.8 实现远程方法调用
"""

"""
11.9 简单的客户端认证
"""

"""
11.10 在网络服务中加入SSL
"""

"""
11.11 进程间传递Socket文件描述符
"""

"""
11.12 理解事件驱动的IO
"""

"""
11.13 发送与接收大型数组
"""