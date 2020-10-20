# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      thread_demo
    Description:
    Author:         Kirk
    Date:           2020/10/20
-----------------------------------------
    Change Activity:
                    2020/10/20
-----------------------------------------
"""
import threading
import time


def run_thread(n):
    print('thread %s is running...' % threading.current_thread().name)
    for _ in range(n):
        time.sleep(1)
        print(_)

    print('thread %s ended.' % threading.current_thread().name)


def run_thread2(n):
    print('thread %s is running...' % threading.current_thread().name)
    time.sleep(n)
    print('stop')
    print('thread %s ended.' % threading.current_thread().name)


t1 = threading.Thread(target=run_thread, args=(10,), name='Thread-1')
t2 = threading.Thread(target=run_thread2, args=(5,), name='Thread-2')
t1.start()
t2.start()
t2.join()
t1.join()
