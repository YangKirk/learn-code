# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      thread_learning
    Description:
    Author:         Kirk
    Date:           2020/10/20
-----------------------------------------
    Change Activity:
                    2020/10/20
-----------------------------------------
"""
import time
import threading


# 1.新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# 2.假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


if __name__ == '__main__':
    pass
    # 1
    # print('thread %s is running...' % threading.current_thread().name)
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.start()
    # t.join()
    # print('thread %s ended.' % threading.current_thread().name)

    # 2
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
