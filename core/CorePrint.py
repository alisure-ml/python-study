# for get current method name
import inspect
from core.CoreTime import CoreTime


# the core class about print
class CorePrint:

    # 组装信息
    @staticmethod
    def __get_string(*args, _separate=" "):
        _result = ""
        for arg in args:
            _result += str(arg) + _separate
        return _result

    # 打印信息
    @staticmethod
    def print_info(*msgs):
        print(CoreTime.get_format_time(), CorePrint.__get_string(*msgs))
        pass

    # 打印信息
    @staticmethod
    def print_info_with_method(arg, *args):
        print(CoreTime.get_format_time(), "method:", inspect.stack()[1][3],
              ",info:", arg, CorePrint.__get_string(*args))
        pass

if __name__ == "__main__":
    CorePrint.print_info("a", 2, "cd")
    CorePrint.print_info_with_method("cccc", "xx", "efdw")

    pass
