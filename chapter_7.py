# /usr/bin/env python
# __author__ = 'P0WER1ISA'
# __homepage__ = 'https://github.com/P0WER1ISA'
# __builddate__:2017/8/9 19:33

# 7.1 编写可接受任意数量参数的函数 (可以使用*号开头的参数)

def fun_t(*n):  # 任意元组参数，只能作为最后一个位置参数出现
    for i in n:
        print(i)


def fun_k(**n):  # 任意关键字参数，只能作为最后一个参数出现
    for k, v in n.items():
        print('{0} : {1}'.format(k, v))


fun_t(1, 2, 3)  # 任意元组参数
fun_t('j', 'jjijfie', 1, 'ej', 'wfe', 4)  # 任意元组参数

fun_k(city='beijing', job='enginner')  # 任意关键字参数


# 7.2 编写只接受关键字参数的函数
def recv(maxsize, *, block):
    pass


recv(1024, block=True)


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))


# 7.3 将元数据信息附加到函数参数上
def add(x: int, y: int) -> int:
    return x + y


help(add)  # 查看函数完整签名
print(add.__annotations__)  # 查看注释


# 7.4 从函数中返回多个值
def myfun():
    return 1, 2, 3


x, y, z = myfun()
print(x)
print(y)
print(z)


# 7.5 定义带有默认参数的函数
def add(x, y=3):
    return x + y


print(add(1, 1))
print(add(1))

# 7.6 定义匿名或内联函数
add = lambda x, y: x + y
print(add(1, 2))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
new_names = sorted(names, key=lambda name: name.split()[-1].lower())
print(new_names)

# 7.7 在匿名函数中绑定变量的值
x = 10
a = lambda y, x=x: x + y  # lambda表达式中的x的值是在执行时确定的，执行时x的值是多少就是多少`1
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

# 7.8 让带有N个参数的可调用对象以较少的参数形式调用 (使用functools.partial())
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


spam(1, 2, 3, 4)  # 常规调用

s1 = partial(spam, 1)
print(s1(2, 3, 4))

s2 = partial(spam, 1, 2, d=42)
print(s2(1))

# 7.9 用函数替代只有单个方法的类(除了init方法之外，单个方法的类，可以通过闭包closure转换为函数)
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template) -> None:
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate('http://finace.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


def urltemplate(template):  # 采用闭包将只有一个方法的类，转换为嵌套函数
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener()


yahoo = urltemplate('http://finace.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


# 7.10 在回调函数中携带额外的状态
def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


apply_async(add, (2, 3), callback=print_result)


# 7.11 内联回调函数
def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
            return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('GoodBye')


test()
