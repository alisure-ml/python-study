import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))

# label : 给所绘制的曲线一个名字，此名字在图示(legend)中显示。
# 只要在字符串前后添加"$"符号，matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
# color : 指定曲线的颜色
# linewidth : 指定曲线的宽度
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=1)
plt.plot(x, z, "b--", label="$cos(x^2)$", linewidth=1)

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
# 设置Y轴范围
plt.ylim(-1.2, 1.2)
# 显示图示
plt.legend()
plt.show()
