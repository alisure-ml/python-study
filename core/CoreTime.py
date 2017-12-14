import time
import functools


# the core class about time
class CoreTime:

    # get time
    @staticmethod
    def get_format_time():
        """
        :return: 2017-05-12 16:24:29
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @staticmethod
    def run_time_wrapper(fn):
        def _wrapper(*args, **kwargs):
            start = time.clock()
            fn(*args, **kwargs)
            print(CoreTime.get_format_time(), fn.__name__, "cost", time.clock() - start, "second")
        return _wrapper

    @staticmethod
    def run_time_wrapper_inf(info=""):
        def _run_time_wrapper(fn):
            @functools.wraps(fn)
            def _wrapper(*args, **kwargs):
                start = time.clock()
                fn(*args, **kwargs)
                print(CoreTime.get_format_time(), info, fn.__name__, "cost", time.clock() - start, "second")
            return _wrapper
        return _run_time_wrapper

    # 运行计时
    @staticmethod
    def run_for_time(_start_time=0):
        """
        time.clock():
            Return the CPU time or real time since the start of the process or since the first call to clock()
        
        use method:
            start_time = CoreTime.run_for_time()
            time.sleep(1)
            end_time = CoreTime.run_for_time(start_time)
            
        :param _start_time: 
        :return: 
        """
        if _start_time == 0:
            return time.clock()
        else:
            return time.clock() - _start_time
        pass


@CoreTime.run_time_wrapper
def run_time():
    print(CoreTime.get_format_time())


@CoreTime.run_time_wrapper_inf(info="hello")
def run_time_2():
    print(CoreTime.get_format_time())

if __name__ == "__main__":
    print(CoreTime.get_format_time())

    run_time()
    run_time_2()

    start_time = CoreTime.run_for_time()
    time.sleep(1)
    end_time = CoreTime.run_for_time(start_time)
    print(CoreTime.get_format_time(), "the cost of time is", end_time)
