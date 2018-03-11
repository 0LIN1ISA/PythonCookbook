# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/11 0:05

"""
第9章 源编程
"""

"""
9.1 在函数上添加包装器
"""
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n: int):
    """this count func"""
    while n > 0:
        n -= 1


print(countdown(100000))

"""
9.2 创建装饰器时保留函数元信息
"""
# @wraps装饰器，可以保留原函数的元信息

print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

"""
9.3 解除一个装饰器
"""
# 如果装饰器是通过@wraps来实现的，我们可以通过访问__wrapped__属性来访问原始函数
from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


add(4, 5)
# 在Python3.3中会忽略所有包装层
# 在Python3.6中，只会忽略最顶层

