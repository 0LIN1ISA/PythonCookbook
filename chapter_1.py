# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "P0WER1ISA"
# Date:2017/7/31 0:04

# 1.1 将序列分解为单独的变量
p = (4, 5)  # tuple type
x, y = p
print('x={0},y={1}'.format(x, y))

data = ['ACME', 50, 91.1, (2012, 12, 2)]  # list type
name, shares, price, date = data
print('name={0},shares={1},price={2},date={3}'.format(name, shares, price, date))
# *注：如果元素的数量不匹配，将得到一个错误提示。

a, b, c, d, e = 'hello'  # 不仅仅元组和列表类型，只要对象是一个可迭代的，那么就可以进行分解操作。例如，字符串
print(a)
print(b)
print(c)
print(d)
print(e)


# 1.2 从任意长度的可迭代对象中分解元素(*表达式)
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


print(drop_first_last(('a', 'b', 'c', 'd', 'e', 'f')))

record = {'Dave', 'dave@example.com', '773-555-1212', '847-555-1212'}
name, email, *phone_numbers = record
print(phone_numbers)

# 1.3 保存最后N个元素(使用collections.deque)
from collections import deque

q = deque(maxlen=3)
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for data in list_data:
    q.append(data)
print(list(q))

# 1.4 找到最大或最小的N个元素(heapq模块的nlargest()函数和nsmallest()函数)
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 43, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 1.5 实现优先级队列
import heapq

list_data = []
heapq.heappush(list_data, 5)
heapq.heappush(list_data, 2)
heapq.heappush(list_data, 8)
heapq.heappush(list_data, 4)
heapq.heappush(list_data, 3)
heapq.heappush(list_data, 7)
print(heapq.heappop(list_data))  # heappop，弹出并返回最小值的项，返回：2
print(heapq.heappop(list_data))  # 3
print(heapq.heappushpop(list_data, 1))  # 向堆里插入一项，并返回最小值的项。返回：1

heap = [19, 9, 4, 10, 11]
heapq.heapify(heap)
print(heap)

# 1.6 在字典中将键映射到多个值上
from collections import defaultdict

d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['a'].append(3)
print(d1['a'])
d2 = {}
d2.setdefault('b', []).append(1)
d2.setdefault('b', []).append(2)
d2.setdefault('b', []).append(4)
print(d2['b'])
print(d1)
print(d2)

# TODO:1.7 让字典保持有序
from collections import OrderedDict

d2 = OrderedDict()
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'
for k, v in d2.items():
    print(k, v)

# 1.8 与字典有关的计算问题
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
min_price = min(zip(prices.values(), prices.keys()))  # 最小值
max_price = max(zip(prices.values(), prices.keys()))  # 最大值
prices_sorted = sorted(zip(prices.values(), prices.keys()))  # 排序
print('min_price:{0}'.format(min_price))
print('max_price:{0}'.format(max_price))
print('prices_sorted:{0}'.format(prices_sorted))

# 1.9 在两个字典中寻找相同点
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
print(a.keys() & b.keys())  # 相同的键
print(a.keys() - b.keys())  # 不同的键
print(a.items() & b.items())  # 相同的键值


# TODO: 1.10 从序列中移除重复项且保持元素间顺序不变
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]  # 可hashable对象，使用（集合和生成器）
print(set(a))  # 顺序发生变化
print(list(dedupe(a)))  # 顺序没有发生变化

# 1.11 对切片命名
record = '....................100 ..........................53.12...............'
SHARES = slice(20, 23)
print(record[SHARES])

# 1.2 找出序列中出现次数最多的元素 (使用collections模块中的Counter类)
words = ['words_1', 'words_2', 'words_2', 'words_1', 'words_2', 'words_4', 'words_2', 'words_3', 'words_1', ]
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)  # 显示出现频率最高的前3个单词
print(top_three)
print(word_counts['words_2'])  # 在底层实现中，Counter是一个字典

# 1.13 通过公共键对字典列表进行排序 (利用operator模块中的itemgetter函数进行排序)
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)


# 1.14 对不原生支持比较操作的对象排序 (使用sorted的key参数)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(56)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

# 1.15 根据字段将记录分组 (itertools.groupby()函数)

rows = [
    {'address': '2612 CN CwefLARK', 'date': '07/02/2012'},
    {'address': '7412 CN CgeLARweK', 'date': '07/02/2012'},
    {'address': '5312 CN Cwwu45eLAegRK', 'date': '07/23/2012'},
    {'address': '4812 CN CwegLAegRK', 'date': '07/02/2012'},
    {'address': '8614 CN CL34egRK', 'date': '07/04/2012'},
    {'address': '2512 CN CLweryeARK', 'date': '07/02/2012'},
    {'address': '6452 CN Cwe4hLAwegRK', 'date': '07/01/2012'},
    {'address': '9427 CN ChLqrARK', 'date': '07/24/2012'},
    {'address': '7335 CN CLqwARK', 'date': '07/23/2012'},
    {'address': '2847 CN CLqerhARK', 'date': '07/01/2012'},
]
from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))  # 以date字段进行排序
print(rows)
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 1.16 筛选列表中的元素
mylist = [1, 4, -5, 2, 8, -10, 8, 6]
print([n for n in mylist if n > 0])  # 列表推导式

mylist2 = ['1', '4', '-5', '2', '8', 'N/A', '-10', '8', '6']  # 简单列表推导式已经不能处理复杂数据


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = [n for n in filter(is_int, mylist2) if int(n) > 0]  # 使用filter过滤数据后，进行处理
print(ivals)

# 1.17 从字典中提取子集

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.37, 'HPQ': 37.20, 'FB': 10.75}

p1 = {key: value for key, value in prices.items() if value > 200}  # 获取过滤字典value值
print(p1)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# 1.18 将名称映射到序列的元素中 (使用collections.namedtuple())
from collections import namedtuple

Subscriber = namedtuple('my_type', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(type(sub))

# 1.19 同时对数据做转换和换算
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

import os

files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry,no python')

# 1.20 将多个映射合并为单个映射 (使用collections中的ChainMap类)
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)  # 相同key的value不会合并
print(c['x'])
print(c['y'])
print(c['z'])
