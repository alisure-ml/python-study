"""
解释器在sys.path（搜索路径）中查找模块。
所以若要让模块可用，可以：
    1. 将模块放到合适的位置，或者
    2. “告诉解释器去哪里查找需要的模块”。
"""
import sys
# 默认的搜索路径
# print(sys.path)

# 在最前面添加自定义路径
sys.path.insert(0, "F:\\pycharm\\File\\python\\python-study\\module\\package")
# print(sys.path)

# 导入自定义的包
import package
from package.python_1 import python_11
from package.python_2 import python_22

# 执行自定义的包
package.python_1.python_11()
package.python_2.python_22()
python_11()
python_22()
