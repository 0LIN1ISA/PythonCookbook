# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "P0WER1ISA"
# Date:2017/8/3 16:10

# 2.1 针对任意多的分隔符拆分字符串
import re  # split()函数只能处理简单的分割，复杂使用re.split模块

line = 'asdf fjkd; afed, fjek,asdf,    foo'

print(re.split(r'[;,\s]\s*', line))

# 2.2 在字符串开头或结尾出做文本匹配
filename = 'span.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))
url = 'http://www.python.org'
print(url.startswith('http://'))

# 利用Shell通配符做字符串匹配 (fnmatch模块的fnmatch()和fnmatchcase())
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'Dat3.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

print(fnmatchcase('foo.TXT', '*.txt'))  # fnmatchcase，区分大小写方式进行匹配

# 2.4 文本模式的匹配和查找 (简单查找用str.find(),str.endswith(),str.startwith，复杂超找用re)
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('yeah'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Now 27, 2012'
import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 2.5 查找和替换文本 (简单用str.replace方法，复杂用re.sub)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

new1_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)  # "\3"标识前面匹配模式中第N个元素
print(new1_text)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')  # compile预编译，提高效率
new2_text = datepat.sub(r'\3-\1-\2', text)
print(new2_text)

# 2.6 以不区分大小写的方式对文本做查找和替换
text = 'UPPER PYTHON, lower python, Mixed Python'
import re

print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 2.7 定义实现最短匹配的正则表达式
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'
import re

print(re.findall(r'\"(.*)\"', text1))
print(re.findall(r'\"(.*)\"', text2))  # (.*) 正则表达式“贪婪”原则
print(re.findall(r'\"(.*?)\"', text2))  # (.*?) 非“贪婪”，“最短”原则

# 2.8 编写多行模式的正则表达式
text = '''/* this is a
            multiline comment */
'''
import re

comment1 = re.compile(r'/\*(.*?)\*/')
print(comment1.findall(text))  # 因为换行了，无法匹配
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')  # 添加对换行符的支持
print(comment2.findall(text))

# TODO:2.9 将Unicode文本统一表示为规范形式
s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapeu\u0303o'
print(s1, s2)  # 两者长的一样，但是不想等
print(s1 == s2)
import unicodedata  # 使用unicodedata进行转换

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, t2)
print(t1 == t2)

# TODO: 2.10 用正则表达式处理Unicode
import re

num = re.compile('\d+')
a = num.match('123')

# 2.11 从字符串去掉不需要的字符
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 2.12 文本过滤和清理 (str.translate()方法)
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)

import unicodedata  # 清理掉unicode组合字符
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs))

# 2.13 对齐文本字符串
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))

# 2.14 字符串连接及合并
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# 2.15 给字符串中的变量名做插值处理
s = '{name} has {n} message.'
print(s.format(name='p0wer1isa', n='34'))

# 2.16 以固定的列数重新格式化文本 (使用textwrap重新格式化)
s = 'Look into my eyes, look into my eyes, the eyes, the eyes, ' \
    'the eyes, not around the eyes, don\'t look around the eyes, ' \
    'look into my eyes, you\'re under. '

import textwrap

print(textwrap.fill(s, 30))
print(textwrap.fill(s, 40, initial_indent='    '))  # 首行缩进
print(textwrap.fill(s, 40, subsequent_indent='    '))  # 全部缩进

# 2.17 在文本中处理HTML和XML实体
s = 'Elements are written as "<tag>text</tag>".'
import html

print(s)
print(html.escape(s))  # HTML转义，反函数unescape

# TODO:2.18 文本分词
text = 'too = 23 + 43 * 100'
import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIME>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
scanner.match().groups()

# TODO:2.19 编写一个简单的递归下降解析器

# 2.20 在字节串上执行文本操作
data = b'Hello World'  # 字节操作
print(data[0:5])
print(data.startswith(b'Hello'))

data_array = bytearray(b'Hello World')  # 字节数组上操作
print(data_array[0:5])
print(data_array.startswith(b'Hello'))

data_reg = b'FOO:BAR,SPAM'
import re

print(re.split(b'[:,]]', data_reg))  # 使用re正则表达式，模式本身页需要以字节指定
