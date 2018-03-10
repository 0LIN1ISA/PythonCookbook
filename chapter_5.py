# /usr/bin/env python
# __author__ = 'P0WER1ISA'
# __homepage__ = 'https://github.com/P0WER1ISA'
# __builddate__:2017/8/8 1:35

# 5.1 读写文本数据
with open('chapter_5.py', 'rt') as f:  # rt：读取文本文件
    data = f.read()

with open('chapter_5.py', 'wt') as f:  # wt：写入文本文件，在文件尾部追加文件使用'at'
    pass
    # f.write('some text')
    # f.write('some text')

import sys

print(type(sys.getdefaultencoding()))
print(sys.getdefaultencoding())  # 获得系统默认编码

# 5.2 将输出重定向到文件中
with open('chapter_5.py', 'wt') as f:
    pass
    # print('Hello World!', file=f) # 将print()函数输出重定向到文件中去

# 5.3 以不同的分隔符或行结尾符完成打印 (使用print的sep和end关键字)
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

# 5.4 读写二进制数据 (使用open函数的'rb'和'wb'模式)
with open('somefile.bin', 'wb') as f:
    data = f.write(b'hello world')

with open('somefile.bin', 'rb') as f:
    data = f.read().decode('utf-8')
    print(data)
    print(data[0])

# 5.5 对已存在的文件执行写入操作
with open('somefile.txt', 'wt') as f:
    f.write('hello\n')

with open('ssomefile.txt', 'xt') as f:
    f.write('hello\n')

# 5.6 在字符串上执行I/O操作
import io

s = io.StringIO()  # 读写文本
s.write('Hello World\n')
print('This is a test', file=s)
print(s.getvalue())
print(s.read(4))

b = io.BytesIO()
b.write(b'Hello')
b.write(' World'.encode("utf-8"))
print(b.getvalue())

# 5.7 读写压缩的数据文件 (gzip和bz2)
import gzip
import bz2

with gzip.open('testfile.gzip', 'wt') as f:  # 写gzip文件
    f.write('this\'s gzip file')

with bz2.open('tsetfile.bz2', 'wt') as f:  # 写bz2文件
    f.write('this\s bz2 file')

with gzip.open('testfile.gzip', 'rt') as f:  # 读gzip文件
    line = f.read()
    print(line)

with bz2.open('tsetfile.bz2', 'rt') as f:  # 读gz2文件
    line = f.read()
    print(line)

# TODO:5.8 对固定大小的记录进行迭代 (使用iter()和functools.partial())
from functools import partial

RECORD_SIZE = 333
with open('chapter_5.py', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')  # functools.partial 通过包装手法，允许我们 "重新定义" 函数签名
    for r in records:
        print(r.decode('utf-8'))

# 5.9　将二进制数据读取到可变缓冲区中 (readinto)
import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)  # 读取到缓冲区，类型：字节数组
    return buf


buf = read_into_buffer('chapter_5.py')
print(buf.decode('utf-8'))
print(buf[0:10].decode('utf-8'))  # 切片操作

# 5.10 对二进制文件做内存映射
import os
import mmap


def memory_map(filename, access=mmap.ACCESS_COPY):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)  # os.O_RDWR，以读写方式打开
    return mmap.mmap(fd, size)  # 返回一个内存映射对象


m = memory_map('chapter_5.py')
print(m.read(20))
m.close()

# 5.11 处理路径名
import os

path = '/Users/Beazley/Data/data.csv'
print(os.path.basename(path))  # 显示文件名
print(os.path.dirname(path))  # 显示路径名
print(os.path.join('tmp', 'data', os.path.basename(path)))  # 整合路径

# 5.12 检测文件是否存在
import os

print(os.path.exists('/etc/passwd'))  # 文件是否存在
print(os.path.isfile('/home/user/abc'))  # 是否是文件
print(os.path.isdir('/home/user/abc/work'))  # 是否是文件夹

# 5.13 获取目录内容的列表
import os

for i in os.listdir('D:\Software'):  # 项目目录下文件及文件夹
    print(i)

for a, b, c in os.walk('D:\Software'):  # 递归显示文件和文件夹
    print(a)
    print(c)

# 5.14 绕过文件名编码
print(sys.getdefaultencoding())  # 显示当前系统默认编码

for x in os.listdir(b'.'):  # 以二进制编码方式来列举目录
    print(x)

# TODO:5.15 打印无法解码的文件名
mystr = "this is string example....wow!!!"
temp = mystr.encode(sys.getdefaultencoding(), 'surrogateescape')

# 5.16 为已经打开的文件添加或修改编码方式 (使用io.TextIOWrapper())
import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)

# 5.17 将字节数据写入文本文件
import sys

# sys.stdout.write(b'Hello\n') # 不能直接使用stdout.write方法
sys.stdout.buffer.write(b'Hello\n')  # 使用stdout.buffer.write方法

# 5.18 将已有的文件描述符包装为文件对象
import os

fd = os.open('chapter_5.py', os.O_RDONLY)
f = open(fd, 'rt', encoding='utf-8')
print(f.read())

# 5.19 创建临时文件和目录 (使用tempfile模块)
from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
    print(data)

# 5.20 同串口进行通信 (使用pySerial)
import serial

ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()

# 5.21 TODO:序列化Python对象 (使用pickle)
try:
    import cPickle as pickle  # cPickle 用C写的Pickle模块，速度更快
except ImportError:
    import pickle


class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self) -> str:
        return 'my name is {0},i age{1},isex:{2}'.format(self.name, self.age, self.sex)


def st_to_dict(p):
    return 'my name is {0},i age{1},isex:{2}'.format(p.name, p.age, p.sex)


import json

p = Person('jack', 25, 'boy')
a = json.dumps(p, default=st_to_dict)  # json.dumps 实现对象实例序列化
print(a)

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
f = open('sesion.bin', 'wb')
pickle.dump(data1, f)  # 实现列表对象序列化
f.close()

open('sesion.bin', 'rb')
data = pickle.load(f)  # 反序列化
print(data)
f.close()

# import time
# import threading
#
#
# class Countdown:
#     def __init__(self, n) -> None:
#         self.n = n
#         self.thr = threading.Thread(target=self.run)
#         self.thr.daemon = True
#         self.thr.start
#
#     def run(self):
#         while self.n > 0:
#             print('T-minus', self.n)
#             self.n -= 1
#             time.sleep(5)
#
#     def __getstate__(self):
#         return self.n
#
#     def __setstate__(self, n):
#         self.__init__(n)
#
#
# c = Countdown(30)
#
# f = open('cstate.p', 'wb')
# import pickle
#
# pickle.dump(c, f)
# f.close()
