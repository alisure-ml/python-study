### 常见错误


#### 命令行中使用`pip3`出错

* 问题

```cmd
C:\Users\ALISURE>pip -V
Traceback (most recent call last):
  File "c:\alisure\python\python3\lib\runpy.py", line 184, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\alisure\python\python3\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\ALISURE\Python\Python3\Scripts\pip3.exe\__main__.py", line 5, in <module>
  File "c:\alisure\python\python3\lib\site-packages\pip\__init__.py", line 26, in <module>
    from pip.utils import get_installed_distributions, get_prog
  File "c:\alisure\python\python3\lib\site-packages\pip\utils\__init__.py", line 27, in <module>
    from pip._vendor import pkg_resources
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 3018, in <module>
    @_call_aside
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 3004, in _call_aside
    f(*args, **kwargs)
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 3046, in _initialize_master_working_set
    dist.activate(replace=False)
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 2578, in activate
    declare_namespace(pkg)
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 2152, in declare_namespace
    _handle_ns(packageName, path_item)
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 2092, in _handle_ns
    _rebuild_mod_path(path, packageName, module)
  File "c:\alisure\python\python3\lib\site-packages\pip\_vendor\pkg_resources\__init__.py", line 2121, in _rebuild_mod_path
    orig_path.sort(key=position_in_sys_path)
AttributeError: '_NamespacePath' object has no attribute 'sort'
```


* 解决方法：修改line 2121~2122

```python
# orig_path.sort(key=position_in_sys_path)
# module.__path__[:] = [_normalize_cached(p) for p in orig_path]
orig_path_t = list(orig_path)
orig_path_t.sort(key=position_in_sys_path)
module.__path__[:] = [_normalize_cached(p) for p in orig_path_t]
```



