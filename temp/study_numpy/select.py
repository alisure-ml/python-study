import numpy as np

print("-" * 50)
arr = np.random.rand(5)
print(arr)
print((arr > 0.5).sum())

print("-" * 50)
print("any和all对布尔型数组非常有用，可以测试数组中是否存在一个或多个True")
bools = np.array([False, False, True])
print(bools.any())
print(bools.all())

print("-" * 50)
arrs = np.random.rand(10)
print(arrs.sum())
print(arrs.min())
print(arrs.argmin())
print(arrs.argmax())

print("-" * 50)
print("用sort函数进行排序")
arrs = np.random.rand(10)
print(arrs)
arrs.sort()
print(arrs)

print("-" * 50)
print("sort函数也可以在某个轴上进行排序，0是列，1是行")
arrs = np.random.randn(3, 2)
print(arrs)
arrs.sort()
print(arrs)
arrs.sort(0)
print(arrs)
arrs.sort(1)
print(arrs)

print("用unique函数唯一化")
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

print("用np.in1d函数测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组")
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))

print("数组的文件输入输出")
arr = np.arange(10)
np.save('some_array',arr)

load = np.load('some_array.npy')
print(load)