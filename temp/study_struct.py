"""
C语言的结构体与python的字符串之间进行转换。
[struct — Interpret bytes as packed binary data](https://docs.python.org/3/library/struct.html)
[python3中的struct模块使用](http://blog.csdn.net/djstavav/article/details/77950352)
"""

import struct


def basic_fun():
    name = b'lily'
    age = 18  # int类型占4个字节
    sex = b'female'
    job = b'teacher'
    fmt = '4si6s7s'

    file_name = "data/study_struct.bin"

    # 将数据按照格式写入文件中
    with open(file_name, 'wb') as fp:
        # 返回按照fmt数据格式组合而成的字符串
        pack_str = struct.pack(fmt, name, age, sex, job)
        fp.write(pack_str)
        fp.flush()

    # 将文件中写入的数据按照格式读取出来
    with open(file_name, 'rb') as fd:
        # 返回按照给定数据格式解开的tuple
        fmt_size = struct.calcsize(fmt)  # 21 = 4 + 4 + 6 + 7
        unpack_tuple = struct.unpack(fmt, fd.read(21))
        print(unpack_tuple)
        print(fmt_size)

    pass


def basic_fun2():

    pack_num = struct.pack(">hhl", 1, 2, 3)
    print(pack_num)

    unpack_num = struct.unpack("<hhl", pack_num)
    print(unpack_num)

    size_num = struct.calcsize(">hhl")  # 2 + 2 + 4
    print(size_num)

    pass


def basic_fun3():
    record = b'raymond   \x32\x12\x08\x01\x08'
    name, serial_num, school, grade_level = struct.unpack('<10sHHb', record)
    print("{}:{}:{}:{}".format(name, serial_num, school, grade_level))
    pass


if __name__ == '__main__':
    basic_fun3()
