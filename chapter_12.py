# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/11 22:38

"""
第12章 并发编程
"""

"""
12.1 启动与停止线程
"""
# 直接通过Thread方法来实现
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()

# 通过继承Thread来实现，只要实现run方法
from threading import Thread


class CountDownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


# c = CountDownThread(5)
# c.start()

# multiprocessing多进程
import multiprocessing

c = CountDownThread(5)
p = multiprocessing.Process(target=c.run)
p.start()

"""
12.2 判断线程是否已经启动
"""
# 使用threading的event对象
from threading import Thread, Event
import time


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = Event()

# launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print('countdown is running')

import threading


def do(event, name):
    print(name + ':start')
    event.wait()
    print(name + ':execute')


event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj, 'thread_' + str(i)))
    t.start()

event_obj.clear()
inp = input('input:')
if inp == 'true':
    event_obj.set()

# event对象通过set会唤醒所有等待他的线程，
# 如果只想唤醒单个线程，可以使用信号量或者Condition
# Worker thread
import threading


def worker(n, sema):
    # wait to be signaled
    sema.acquire()

    # do some work
    print('working', n)


# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

sema.release()
sema.release()

"""
12.3 线程间通信
"""
# 通过Queue的put()和get()来操作
from queue import Queue
from threading import Thread


def producer(out_q):
    while running:
        for i in range(100):
            out_q.put(i)


def consumer(in_q):
    while True:
        data = in_q.get()
        print(data)

        in_q.task_done()


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()

q.join()

"""
12.4 给关键部分加锁
"""