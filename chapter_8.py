# /usr/bin/env python
# __author__ = '0LIN1ISA'
# __homepage__ = 'https://github.com/0LIN1ISA'
# __writedate__:2017/8/15 23:11

# 8.1 修改实力的字符串表示 (通过__str__()和__repr__()函数)
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # 要能满足 eval(repr(x)) == x
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)


p = Pair(3, 4)
print(p)  # __str__() output

f = open('chapter_8.py')
print(f)
print(f.__repr__())
print(f.__str__())


# 8.2 自定义字符串输出格式 (通过__format__()函数)
class Date:
    _formats = {'ymd': '{d.year}-{d.month}-{d.day}', 'mdy': '{d.month}/{d.day}/{d.year}',
                'dmy': '{d.day}/{d.month}/{d.year}'}

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = self._formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(format(d))
print(format(d, 'mdy'))
print(format(d, 'dmy'))
print('The date is {:mdy}'.format(d))
print('The date is {:ymd}'.format(d))

# 8.3 让对象支持上下文管理协议(需要实现__enter__()和__exit__()方法)
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed


# 8.4 创建大量实例时如何节省内存
class Date:
    __slots__ = ['year', 'month', 'day']  # 当定义了__slots__属性时，Python将会针对实例采用一种更加紧凑的内部标识。

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# 8.5 将名称封装到类中
class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        """
        A public method
        :return:

        """

    def _internal_method(self):  # 任何以单下划线开头的名字总是被认为只属于内部实现。
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):  # 以双下划线开头的名字会导致出现名称重整(name mangling)的行为。子类不能通过继承来覆盖。
        pass

    def public_method(self):
        self.__private_method()


# 8.6 创建可管理的属性
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can\'t delete attribute')


a = Person('Guido')
print(a.first_name)
a.first_name(443)
del a.first_name


# 8.7 调用父类中的方法
class A:
    def spam(self):
        print('A.spam')


class B:
    def spam(self):
        print('B.spam')
        super().spam()  # super()函数的一种常见用途是调用父类的__init__()方法，确保父类被正确初始化


# 8.8 在子类中扩展属性
class Person():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')

    @property.deleter
    def name(self):
        raise AttributeError('Can\'t delete attribute')


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        return super(SubPerson, self).name()
        print('Getting name')

    @Person.name.setter
    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


# 8.9 创建一种新形式的类属性和实例属性
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            instance.__dict__[self.name]  # __dict__属性存储对象的属性

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
