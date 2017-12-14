import multiprocessing

# 数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15]


# 进程中需要执行的任务
def my_target(begin, end, index):
    print("%d-[%d %d]" % (int(index), int(begin), int(end)))
    for i in range(int(begin), int(end)):
        print(data[i])


def demo_process():
    # CPU数量
    cpu_number = multiprocessing.cpu_count()
    # 每个进程需要执行的数据个数
    each_number = len(data) // cpu_number

    # 用于保存进程
    processes = []

    # 遍历所有的CPU
    for index in range(cpu_number):
        # 开始
        begin = index * each_number
        # 结束
        end = len(data) if index == cpu_number - 1 else begin + each_number
        # 新建进程
        process = multiprocessing.Process(target=my_target, args=(str(begin), str(end), str(index)))
        # 启动进程
        process.start()
        # 保存进程
        processes.append(process)

    # 等待所有的进程结束
    for p in processes:
        p.join()


if __name__ == '__main__':
    demo_process()
