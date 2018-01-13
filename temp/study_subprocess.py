"""
subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。

subprocess模块提供了一种一致的方法来创建和处理附加进程,与标准库中的其它模块相比，提供了一个更高级的接口。
用于替换如下模块：os.system(), os.spawnv(), os和popen2模块中的popen()函数，以及 commands().
"""
import subprocess


# 1.运行外部命令
# call方法可以用于执行一个外部命令，但该方法不能返回执行的结果
# 只能返回执行的状态码： 成功（0）或 错误（非0）
# call()方法中的command可以是一个列表，也可以是一个字符串，作为字符串时需要用原生的shell来执行。
def func_1():
    result = subprocess.call("dir", shell=True)
    print(result)
    pass


# 2.错误处理
def func_2():
    try:
        subprocess.check_call("dir2", shell=True)
    except subprocess.CalledProcessError as err:
        print(err)
    pass


# 3.捕获输出结果
# call()方法启动的进程，其标准输入输出会绑定到父进程的输入和输出。
# 调用程序无法获取命令的输出结果。但可以通过check_output()方法来捕获输出。
def func_3():
    output = subprocess.check_output("dir", shell=True)
    print(output.decode("gbk"))
    pass


# 4.直接处理管道：与进程的单向通信
def func_4():
    # 1.直接执行命令输出到屏幕上
    subprocess.Popen("dir", shell=True)

    # 2.不输出到屏幕,输出到变量
    # 通过Popen()方法调用命令后执行的结果,可以设置stdout值为PIPE，再调用communicate()获取结果返回结果为tuple.
    process = subprocess.Popen(["echo", "trsdsdadwd"], shell=True, stdout=subprocess.PIPE)
    # communicate返回标准输出或标准出错信息
    stdout_value = process.communicate()
    print(stdout_value[0].decode())

    # 3.将结果输出到文件
    with open("communicate.txt", "w+") as f:
        subprocess.Popen("dir", shell=True, stdout=f)
        pass
    pass


# 5.直接处理管道：与进程的双向通信
def func_5():
    process = subprocess.Popen("python", shell=True,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg = "print('Hello ALISURE')".encode()
    process.stdin.write(msg)

    # Popen.communicate()方法用于和子进程交互：发送数据到stdin，并从stdout和stderr读数据，直到收到EOF。
    stdout_value, stderr_value = process.communicate()
    print(stdout_value.decode())
    print(stderr_value.decode("gbk"))
    pass


# 6.创建进程
def func_6():
    return_code = subprocess.call("demo.exe -a", shell=True)
    print(return_code)
    pass

if __name__ == '__main__':
    func_1()
