# /usr/bin/env python
# __author__ = 'P0WER1ISA'
# __homepage__ = 'https://github.com/P0WER1ISA'
# __builddate__:2017/8/9 12:44

# 6.1 读写CSV数据
import csv
from collections import namedtuple

with open('data/stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)  # 读取成元组序列
    print(headings)
    Row = namedtuple('Row', headings)  # 生成csv的列表名称来访问元素内容的tuple子类

    for r in f_csv:  # row是一个元组，包含了一行的列元素(csv文件每列数据用逗号分割)
        row = Row(*r)
        print(row)
        print(r)

with open('data/stocks.csv') as f:
    f_csv = csv.DictReader(f)  # 读取成字典序列
    for row in f_csv:
        print(row)
        print(row['Symbo'])  # 通过行标头来访问每个元素

headers = ['Symbo', 'Price', 'Date', 'Time', 'Chage', 'Volume']
rows = [
    ('AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'),
    ('AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'),
    ('AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'),
    ('AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'),
]
with open('data/stocks_w.csv', 'w') as f:  # 写入csv文件
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)

# 6.2 读写JSON数据
import json

data = {'name': 'ACME', 'shares': 100, 'price': 524.31}
json_str = json.dumps(data)  # JSON序列化
print(json_str)

print(json.loads(json_str))  # JSON反序列化

# 6.3 解析简单的XML文档 (xml.etree.ElementTree)
from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)

# 6.4 以增量方式解析大型XML文件 (考虑使用迭代器和生成器)
from xml.etree.ElementTree import iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)

    tag_stack = []
    elem_stack = []

    for event, elem in doc:
        if event == 'statr':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


# 6.5 将字典转换为XML
from xml.etree.ElementTree import Element


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e)
from xml.etree.ElementTree import tostring  # 使用tostring函数将其转换为字符串

print(tostring(e))
e.set('_id', '1234')  # 增加属性
print(tostring(e))

# 6.6 解析、修改和重写XML
from xml.etree.ElementTree import parse, Element  # 使用ElementTree来读取这个文档，并对其结构作出修改

doc = parse('pred.xml')
root = doc.getroot()
print(root)
root.remove(root.find('sri'))
root.remove(root.find('cr'))
root.getchildren().index(root.find('nm'))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# 6.7 用命名空间来解析XML文档

# 6.8 同关系型数据库进行交互
import sqlite3

db = sqlite3.connect('data/databas.db')
c = db.cursor()
c.execute('CREATE TABLE portfolio (symbol TEXT, shares INTEGER, price REAL)')
db.commit()

# 6.9 编码与解码十六进制数字
s = b'Hello'
import binascii

h = binascii.b2a_hex(s)  # 二进制转十六进制(每个字节的数据转成相应的2位十六进制标识)
print(h)

a = binascii.a2b_hex(h)  # 与b2a_hex函数相反，把买个2位十六进制转成一个2进制字节
print(a)

import base64

s = b'Hello'
h = base64.b16encode(s)  # 同binascii.b2a_hex　，输出大写形式
print(h)
print(base64.b16decode(h))  # 同b2a_hex函数

# Base64编码和解码
import base64

s = b'Hello'
print(s)
a = base64.b64encode(s)  # base64编码
print(a)
print(base64.b64decode(a))  # base64解码

# 6.11 读写二进制结构的数组
from struct import Struct


def write_records(records, format, f):
    records_struct = Struct(format)
    for r in records:
        f.write(records_struct.pack(*r))


records = [(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7)]
with open('data/data.b', 'wb') as f:
    write_records(records, '<idd', f)  # '<'：采用小端存储,'i'：int,'d':double

# 6.12 读取嵌套性和大小可变的二进制结构

# 6.13 数据汇总和统计
