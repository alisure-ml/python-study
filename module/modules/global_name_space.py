"""
每个函数都有自己的命名空间。
类的方法的作用域规则和通常函数的一样。
Python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
因此，如果要给全局变量在一个函数里赋值，必须使用global语句。
"""
var = 1


# 改变的是局部变量的值
def var_local():
    var = 2


# 改变的是全局变量的值
def var_global():
    # global VarName的表达式告诉Python，VarName是一个全局变量，不需要在局部命名空间里寻找这个变量了。
    global var
    var = 2

print(var)

# 改变的是局部变量的值
var_local()
print(var)

# 改变的是全局变量的值
var_global()
print(var)
