# /usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2017/8/6 20:09
# __author__ = 'P0WER1ISA'
# __homepage__ = 'https://github.com/P0WER1ISA'

# 4.1 手动访问迭代器中的元素 (使用next()函数)
with open('README.md', 'rb') as f:
    try:
        while True:
            line = next(f).decode('utf-8')
            print(line)
    except StopIteration:  # 迭代结束，触发StopIteration
        pass

with open('README.md', 'rb') as f:
    try:
        while True:
            line = next(f).decode('utf-8')
            if line is None:  # 迭代结束，返回None
                break
            print(line)
    except Exception:
        pass


# 4.2 委托迭代 (自定义对象实现迭代能力，类实现__iter__()方法即可)
class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)


# 4.3 用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 10, 0.3):
    print(n)


# TODO:4.4 实现迭代协议
class Node():
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node ({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)

# 4.5 反向迭代 (使用内建的reversed)
a = [1, 2, 3, 4, 5, 6]
for x in reversed(a):  # 反向迭代的条件：1：对象元素数量确定 或者 2：实现了__reversed__()特殊方法
    print(x)


class Countdown:
    def __init__(self, start) -> None:
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1


a = Countdown(8)
for x in reversed(a):
    print(x)

# 4.6 定义带有额外状态的生成器函数
from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):  # 设置索引从1开始，默认从0
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('chapter_4.py', 'rt', encoding='utf-8') as f:  # 自动迭代
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

f = open('chapter_4.py', 'rt', encoding='utf-8')  # 手动迭代
lines = linehistory(f)
it = iter(lines)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# 对迭代器做切片操作 (使用itertools.islice()函数来对迭代器和生成器做切片操作)
def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:20]  # 普通切片操作无法进行
import itertools

for x in itertools.islice(c, 10, 15):
    print(x)

# 4.8 跳过可迭代对象中的前一部分元素 (使用itertools.dropwhile()函数)
from itertools import dropwhile

with open('chapter_4.py', encoding='utf-8') as f:
    # 如果predicate为True，就丢弃iterable中的项，如果predicate返回False，就会生成iterable中的项和所有后续项。
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end='')

# 迭代所有可能的组合或排列 (itertools.permutations)
a = ['a', 'b', 'c', 'd']
from itertools import permutations

for i in permutations(a):
    print(i)

# 4.10 以索引-值对的形式迭代序列 (使用内建函数enumerate())
my_list = ['a', 'b', 'c', 'd']
for id, val in enumerate(my_list, 1):
    print('{}:{}'.format(id, val))

# 4.11 同时迭代多个序列
xpts = [1, 2, 3, 4]
ypts = [5, 6, 7, 8, 9, 10, 11]
for x, y in zip(xpts, ypts):  # zip函数创建出一个新的迭代器，多出的元素会被丢弃
    print(x, y)

from itertools import zip_longest  # zip函数的变种，缺少元素会用None填补

for x, y in zip_longest(xpts, ypts):
    print(x, y)

# 4.12 在不同容器中进行迭代 (使用itertools.chain)
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

# 4.13 创建处理数据的管道 (使用生成器函数)
import os
import fnmatch


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


for i in gen_find('*sys*', 'c:\\windows'):
    print(i)

# 4.14 扁平化处理嵌套序列 (使用yield from，yield from iterable本质上等于for item in iterable: yield item的缩写版)
items = [1, 2, [3, 4, [5, 6], 7], 8]  # 嵌套序列
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)  # PEP 380 中新增（Python3.3）
        else:
            yield x


for x in flatten(items):
    print(x)

# 合并多个有序序列，再对整个有序序列进行迭代
import heapq  # 堆排序

a = [1, 4, 7, 10]
b = [2, 5, 6, 9]
for c in heapq.merge(a, b):
    print(c)

# 用迭代器取代while循环
CHUNKSIZE = 8291


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == 'b':
            break
        print(data)


import sys

f = open('chapter_4.py', encoding='utf-8')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
