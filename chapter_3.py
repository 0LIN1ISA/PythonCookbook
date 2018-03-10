# /usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2017/8/4 15:05
# __author__ = 'P0WER1ISA'
# __github__ = 'https://github.com/P0WER1ISA'

# 3.1 对数值进行取整 (使用内建函数round)
print(round(1.23, 1))  # 取整操作
print(round(4.42, 0))
print(round(3.1315, 3))  # 不要使用取整函数来进行“修正”精度，这里没有四舍五入。使用decimal模块
print(round(int(34.24)))  # 转换int

x = 1.234567
print(format(x, '0.2f'))  # 格式化操作
print(format(x, '0.3f'))  # f:float 0.3=保留3位小数

# 3.2 执行精确的小数计算
a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)  # False 误差由底层CPU的浮点运算单元和IEEE 754 浮点数算术标准的一种“特性”
from decimal import Decimal  # 使用decimal的Decimal方法来进行小数计算

a = Decimal('4.2')  # 数字以字符串形式录入
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

from decimal import localcontext  # 进行四舍五入

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:  # localcontext 需要上下文环境，设置prec属性，保留小数位数
    ctx.prec = 3
    print(a / b)

# 3.3 对数值最格式化输出
x = 1234.56789
print(format(x, '0.2f'))  # f:float 浮点数
print(format(x, '0.2e'))  # e:科学计数
print(format(x, '>12.1f'))  # >：靠右对齐，12：输出字符宽度，.1：保留一位小数，f：以float表示
print(format(x, '<8.1f'))  # <：靠左对齐
print(format(x, '<8.1f'))  # <：靠左对齐
print(format(x, ','))
print(format(x, '0,.1f'))

# 3.4 同二进制、八进制和十六进制数打交道
x = 1234
print(bin(x))  # 二进制，以'0b'开头
print(oct(x))  # 八进制，以'0o'开头
print(hex(x))  # 十六进制，以'0x'开头
print(format(x, 'b'))  # 去掉'0b'的二进制

print(int('4d2', 16))  # 用int函数，将字符串形式的整数转换为不同的进制
print(int('10011010010', 2))  # 以2进制方式转换

# 3.5 从字节串中打包和解包大整数
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'  # 16个元素的字节串
print(len(data))
print(int.from_bytes(data, 'little'))  # 将字节转换为整型
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# 3.6 复数运算 (复数是实属的延伸。实数是复数的真子集。实数=有理数+无理数。有理数=整数，0或分数。无理数=无限不循环小数)
a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real)  # 复数实部
print(b.imag)  # 复数虚部
print(b.conjugate())  # 复数共轭值
import cmath

print(cmath.sin(a))  # 复数求正弦
print(cmath.cos(b))  # 复数求余弦
print(cmath.exp(a))  # 复数求平方根

# 3.7 处理无穷大和NaN
from numpy import inf  # numpy模块中的inf，标识无穷数
import math

a = float(inf)
b = float(-inf)
c = float(inf * 0)
print(a is inf)
print(math.isinf(a))  # math模块中的isinf函数，判断是否是inf
print(math.isnan(b))
print(math.isnan(c))

# 分数的计算
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a)
print(a + b)
c = a * b
print(c)
print(a.numerator)
print(a.denominator)
print(float(c))

# 3.9 处理大型数组的计算
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
print(x * 2)
import numpy as np

ax = np.array([4, 2, 5, 1])
ay = np.array([4, 5, 6, 7])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


def f(x):
    return 3 ** 2 - 2 * x + 7


print(f(ax))
print(np.sort(ax))
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid + 10)
print(np.sinc(grid))

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1])  # select row 1
print(a[:, 1])  # select column 1
print(a[1:3, 1:2])

# 3.10 矩阵和线性代数的计算
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print(m.T)
print(m.I)

# 3.11 随机选择
import random

values = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(values)  # 打乱序列顺序
print(values)
print(random.choice(values))  # 随机取出1个元素
print(random.sample(values, 2))  # 随机取出2个元素
print(random.randint(44, 244))  # 获得一个随机整数

# 3.2 时间换算
from datetime import timedelta  # 计算时间间隔

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds())

from datetime import datetime  # 表示日期和时间

a = datetime(2017, 8, 6)
print(a + timedelta(days=10))
b = datetime(2018, 8, 6)
d = b - a
print(d.days)
now1 = datetime.today()
now2 = datetime.now()

print(now1 + timedelta(minutes=10))
print(now2)

# 计算上周5的日期
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()  # 6
    day_num_target = weekdays.index(dayname)  # 'Sunday'
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_go = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today().weekday())  # datetime类的weekday()方法可以获得datetime是星期几,注意weekday() 返回的是0-6是星期一到星期日
print(weekdays.index('Sunday'))
print(get_previous_byday('Monday'))
print(get_previous_byday('Sunday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

# 3.14 找出当月的日期范围
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 3.15 将字符串转换为日期
from datetime import datetime

text = '2012-9-02'
y = datetime.strptime(text, '%Y-%m-%d')
print(type(y), y)

print(datetime.strftime(datetime.now(), '%A %B %d, %Y'))  # 将日期格式化

# 3.16 处理设计到时区的日期问题 (使用pzty模块)
from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 31, 9, 30, 0)
print(d)
central = timezone('US/Central')  # 设置时区
loc_d = central.localize(d)  # 时区当地时间
print(loc_d)
