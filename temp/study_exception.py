

# try except
def try_except():
    try:
        print(1/0)
    # except ZeroDivisionError, e:  # python2
    except ZeroDivisionError as e:  # python3
        print(e)
    pass


# try except else
def try_except_else():
    try:
        print(1/1)
    except ZeroDivisionError as e:
        print("try_except_else {}".format(e))
    else:
        print("try_except_else ok")
    pass


# try excepts else
def try_excepts_else():
    try:
        a = []
        print(a[1/1])
    except ZeroDivisionError as e:
        print("try_excepts_else ZeroDivisionError {}".format(e))
    except IndexError as e:
        print("try_excepts_else IndexError {}".format(e))
    except Exception as e:
        print("try_excepts_else Exception {}".format(e))
    else:
        print("try_excepts_else ok")
    pass


# try excepts else finally
def try_excepts_else_finally():
    try:
        a = []
        print(a[1/1])
    except ZeroDivisionError as e:
        print("try_excepts_else ZeroDivisionError {}".format(e))
    except IndexError as e:
        print("try_excepts_else IndexError {}".format(e))
    except Exception as e:
        print("try_excepts_else Exception {}".format(e))
    else:
        print("try_excepts_else ok")
    finally:
        print("try_excepts_else over")
    pass


# try excepts else finally raise
def try_excepts_else_finally_raise():
    try:
        a = []
        raise Exception("hhhhhhhhhh")
        print(a[1/1])
    except ZeroDivisionError as e:
        print("try_excepts_else ZeroDivisionError {}".format(e))
    except IndexError as e:
        print("try_excepts_else IndexError {}".format(e))
    except Exception as e:
        print("try_excepts_else Exception {}".format(e))
    else:
        print("try_excepts_else ok")
    finally:
        print("try_excepts_else over")
    pass


# 自定义异常
class MyException(BaseException):

    def __init__(self, msg):
        self.msg = msg
        pass

    def __str__(self):
        return self.msg

    pass


# 捕获自定义异常
def try_except_my():
    try:
        raise MyException("my exception")
    except MyException as e:
        print(e)
    pass


if __name__ == '__main__':
    try_except()
    try_except_else()
    try_excepts_else()
    try_excepts_else_finally()
    try_excepts_else_finally_raise()
    try_except_my()
