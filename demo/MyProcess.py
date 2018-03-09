import multiprocessing
from multiprocessing import queues
from core.CorePrint import CorePrint
import time
import os


class Common:

    @staticmethod
    def run_body(name, sleep_time):
        CorePrint.print_info("Process", str(name), "is sleep")
        time.sleep(sleep_time)
        CorePrint.print_info("Process", str(name), "is over")

    pass


# 将进程定义为类
class MyProcess(multiprocessing.Process):
    def __init__(self, name, sleep_time):
        multiprocessing.Process.__init__(self, name=name)
        self.sleep_time = sleep_time

    def run(self):
        Common.run_body(self.name, self.sleep_time)
        pass

    pass


# 当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突
class MyProcessWithLock(multiprocessing.Process):
    def __init__(self, name, sleep_time, lock):
        multiprocessing.Process.__init__(self, name=name)
        self.sleep_time = sleep_time
        self.lock = lock

    def run(self):
        Common.run_body(str("b 1 ") + self.name, self.sleep_time)

        # when run there, if lock, then wait, else run
        with self.lock:
            Common.run_body(self.name, self.sleep_time)

        Common.run_body(str("e 1 ") + self.name, self.sleep_time)

        # another way to use lock
        self.lock.acquire()
        try:
            Common.run_body(str("b 2 ") + self.name, self.sleep_time)
        finally:
            self.lock.release()

        Common.run_body(str("e 2 ") + self.name, self.sleep_time)

        pass
    pass


# Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。
class MyProcessWithSemaphore(multiprocessing.Process):
    def __init__(self, name, sleep_time, semaphore):
        multiprocessing.Process.__init__(self, name=name)
        self.sleep_time = sleep_time
        self.semaphore = semaphore

    def run(self):
        self.semaphore.acquire()
        Common.run_body(self.name, self.sleep_time)
        self.semaphore.release()
        pass
    pass


# Event用来实现进程间同步通信。
class MyProcessWithEvent(multiprocessing.Process):
    def __init__(self, name, sleep_time, event):
        multiprocessing.Process.__init__(self, name=name)
        self.sleep_time = sleep_time
        self.event = event

    def run(self):
        CorePrint.print_info(self.name, str(self.event.is_set()))
        # Wait exe event.set() before run.
        # When timeout, continue run.
        # This is to say, wait and only wait t time before run.
        self.event.wait(self.sleep_time)
        CorePrint.print_info(self.name, str(self.event.is_set()))
        pass
    pass


# Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
class MyProcessWithQueuePut(multiprocessing.Process):
    def __init__(self, name, queue, size):
        multiprocessing.Process.__init__(self, name=name)
        self.queue = queue
        self.size = size

    def run(self):
        try:
            for i in range(self.size):
                # 如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
                # 如果blocked为True（默认值），并且timeout为正值，
                # 该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
                # 如果超时，会抛出Queue.Full异常。
                self.queue.put(i, block=True, timeout=1)
                CorePrint.print_info("put", i, "ok")
        except queues.Full:
            CorePrint.print_info("except queues.Full")
            pass
        pass
    pass


class MyProcessWithQueueGet(multiprocessing.Process):
    def __init__(self, name, queue):
        multiprocessing.Process.__init__(self, name=name)
        self.queue = queue

    def run(self):
        try:
            time.sleep(0.001)
            while True:
                # 如果blocked为False，有两种情况存在:
                # 如果Queue有一个值可用，则立即返回该值，
                # 否则，如果队列为空，则立即抛出Queue.Empty异常。
                # 如果blocked为True（默认值），并且timeout为正值，
                # 那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。
                value = self.queue.get(block=True, timeout=1)
                CorePrint.print_info("get", value, "ok")
        except queues.Empty:
            CorePrint.print_info("except queues.Empty")
            pass


# Pipe
# Pipe方法返回(conn1, conn2)代表一个管道的两个端.
# Pipe方法有duplex参数:
#   duplex为True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发。
#   duplex为False，conn1只负责接受消息，conn2只负责发送消息。
# send和recv方法分别是发送和接受消息的方法。
class MyProcessWithPipe(multiprocessing.Process):
    def __init__(self, name, pipe, is_send_pipe, size):
        multiprocessing.Process.__init__(self, name=name)
        self.pipe = pipe
        self.is_send_pipe = is_send_pipe
        self.size = size

    def run(self):
        if self.is_send_pipe:
            for i in range(self.size):
                self.pipe.send(i)
                CorePrint.print_info("send", i, "ok")
            pass
        else:
            while True:
                r = self.pipe.recv()
                CorePrint.print_info("recv", r, "ok")
            pass

    pass


def run_my_process():
    p1 = MyProcess(name="1", sleep_time=5)
    p2 = MyProcess(name="2", sleep_time=5)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    pass


def run_my_process_with_lock():
    lock = multiprocessing.Lock()
    p1 = MyProcessWithLock(name="3", lock=lock, sleep_time=3)
    p2 = MyProcessWithLock(name="4", lock=lock, sleep_time=3)
    p1.start()
    p2.start()

    pass


def run_my_process_with_semaphore():
    semaphore = multiprocessing.Semaphore(value=2)
    p1 = MyProcessWithSemaphore(name="5", semaphore=semaphore, sleep_time=3)
    p2 = MyProcessWithSemaphore(name="6", semaphore=semaphore, sleep_time=3)
    p3 = MyProcessWithSemaphore(name="7", semaphore=semaphore, sleep_time=3)
    p1.start()
    p2.start()
    p3.start()

    pass


def run_my_process_with_event():
    event = multiprocessing.Event()

    p1 = MyProcessWithEvent(name="5", event=event, sleep_time=2)
    p2 = MyProcessWithEvent(name="6", event=event, sleep_time=2)
    p3 = MyProcessWithEvent(name="7", event=event, sleep_time=6)
    p1.start()
    p2.start()
    p3.start()

    time.sleep(4)
    event.set()

    pass


def run_my_process_with_queue():

    size = 1000
    queue = multiprocessing.Queue(maxsize=size)

    p1 = MyProcessWithQueuePut(name="8", queue=queue, size=size)
    p2 = MyProcessWithQueueGet(name="9", queue=queue)

    p2.start()
    p1.start()

    p1.join()
    p2.join()

    pass


def run_my_process_with_pipe():

    size = 10
    pipe = multiprocessing.Pipe(duplex=False)

    p1 = MyProcessWithPipe(name="10", pipe=pipe[0], is_send_pipe=False, size=size)
    p2 = MyProcessWithPipe(name="11", pipe=pipe[1], is_send_pipe=True, size=size)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    pass


def fun(name, sleep_time):
    CorePrint.print_info(name, "pool in ", os.getpid())
    time.sleep(sleep_time)
    CorePrint.print_info(name, "pool out ", os.getpid())
    return str(name) + " over"
    pass


# 常用的
def run_my_process_with_pool():
    pool = multiprocessing.Pool(processes=3)

    # 关注结果
    results = []

    for i in range(5):
        # 非阻塞
        # pool.apply_async(func=fun, args=(i, i))

        # 阻塞
        # pool.apply(func=fun, args=(i, i))

        # 关注结果
        results.append(pool.apply_async(func=fun, args=(i, i)))

        pass

    CorePrint.print_info("pool close")

    # 关闭pool，使其不在接受新的任务。
    pool.close()
    # 主进程阻塞，等待子进程的退出，join方法要在close或terminate之后使用。
    pool.join()

    # 关注结果
    CorePrint.print_info("pool over")
    for result in results:
        CorePrint.print_info(result.get())

    pass


if __name__ == '__main__':
    run_my_process_with_semaphore()

    pass
