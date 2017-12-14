import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01)

plt.figure(figsize=(8, 4))

line, = plt.plot(x, x * x)
line.set_antialiased(False)

lines = plt.plot(x, np.sin(x), x, np.cos(x))
# 设置属性
plt.setp(lines, color="r", linewidth=1, antialiased=True)
# 获取属性
print(plt.getp(lines[0]))

# 获取当前的绘图对象
f = plt.gcf()
print(plt.getp(f))

plt.show()
