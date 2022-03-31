#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import threading


# 主线程不等待子线程.各个线程自己执行自己的.所以线程执行结束才结束
def 普通线程演示():
    """
    在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务，比如下面的例子：
    Returns:

    """

    def doWaiting():
        print('子线程开始:', time.strftime('%H:%M:%S'))
        time.sleep(3)
        print('子线程结束', time.strftime('%H:%M:%S'))

    t = threading.Thread(target=doWaiting)
    t.start()
    # 确保线程t已经启动
    time.sleep(.1)
    print('主线程开始干活')
    print('主线程干完下班')


# 主线程等待子线程执行结束后在执行。join方式
def 主线程等待子线程():
    def doWaiting():
        print('子线程开始: ', time.strftime('%H:%M:%S'))
        time.sleep(3)
        print('子线程结束: ', time.strftime('%H:%M:%S'))

    print('主线程启动')
    t = threading.Thread(target=doWaiting)
    t.start()
    # 确保线程t已经启动
    time.sleep(.1)
    print('子线程插入')
    # 将一直堵塞，直到t运行结束。
    t.join()
    print('子线程结束')
    print('主线程结束')


# 主线程执行结束就会关闭任务.不会等待子线程结束. setDaemon(True)
def 守护线程演示():
    """
    守护线程会随着主线程的关闭而关闭。
    Returns:

    """

    def run():
        print(threading.currentThread().getName(), '开始工作')
        time.sleep(2)
        print('子线程工作完毕')

    for i in range(3):
        t = threading.Thread(target=run, )
        t.setDaemon(daemonic=True)  # 将子线程设置为守护线程。必须在start()之前设置
        t.start()

    time.sleep(1)  # 主线程暂停1s
    print('主线程结束！ ')
    print(f'当前活跃的线程数量：{threading.active_count()}')  # 输出活跃的线程数


# 线程之间数据污染演示
def 脏数据():
    number = 0

    def plus():
        nonlocal number  # 声明此处的number是外面的变量number
        for _ in range(1000000):  # 进行一个大数级别的百万循环加一运算
            number += 1
        print(f"子线程{threading.current_thread().getName()}运算结束后，number = {number}")

    for i in range(2):  # 用2个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus)
        t.start()

    time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)


# 同一时刻只有一个线程可以访问共享的数据。
def 互斥锁lock():
    number = 0
    lock = threading.Lock()

    def plus(lk):
        nonlocal number
        lk.acquire()
        for _ in range(1000000):
            number += 1

        print(f'子线程{threading.current_thread().getName()}运算结束后，number = {number}')
        lk.release()  # 释放锁，让别的线程也可以方位number

    for i in range(3):
        t = threading.Thread(target=plus, args=(lock,))  # 需要把锁当做参数传递给plus函数
        t.start()
    time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算。
    print(f'主线程执行完毕后，number = {number}')


# 信号Semaphore：允许一定数量的线程同时更改数据
def 信号semaphore():
    def run(n, se):
        se.acquire()
        print("run the thread: %s" % n)
        time.sleep(1)
        se.release()

    # 设置允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(i, semaphore))
        t.start()


# 事件event：通过event来定义线程的开始，暂停和执行
def 事件event():
    event = threading.Event()

    def lighter():  # 控制执行事件
        green_time = 5  # 绿灯时间
        red_time = 5  # 红灯时间
        event.set()  # 初始设为绿灯
        while True:
            print("\33[32;0m 绿灯亮...\033[0m")
            time.sleep(green_time)
            event.clear()
            print("\33[31;0m 红灯亮...\033[0m")
            time.sleep(red_time)
            event.set()

    def run(name):  # 根据lighter的控制执行
        while True:
            if event.is_set():  # 判断当前是否"放行"状态
                print("一辆[%s] 呼啸开过..." % name)
                time.sleep(1)
            else:
                print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
                event.wait()
                print("[%s] 看到绿灯亮了，瞬间飞起....." % name)

    if __name__ == '__main__':

        light = threading.Thread(target=lighter, )
        light.start()

        for name in ['奔驰', '宝马', '奥迪']:
            car = threading.Thread(target=run, args=(name,))
            car.start()


if __name__ == '__main__':
    pass
    # 普通线程演示()
    # 主线程等待子线程()
    # 守护线程演示()
    # 脏数据()
    # 互斥锁lock()
    # 信号semaphore()
    事件event()