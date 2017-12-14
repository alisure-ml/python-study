### __all__

> __all__不仅在第一时间展现了模块的内容大纲，而且也更清晰的提供了外部访问接口。

* 在模块(*.py)中使用：导出__all__列表里的类、函数、变量等成员，
    否则将导出module中所有不以下划线开头（私有）的成员。

* 在包的__init__.py中使用：导出包里的模块。

### Reference

* [https://www.cnblogs.com/alamZ/p/6943869.html](https://www.cnblogs.com/alamZ/p/6943869.html)

* [http://blog.csdn.net/nivana999/article/details/39620673](http://blog.csdn.net/nivana999/article/details/39620673)
