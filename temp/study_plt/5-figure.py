import matplotlib.pyplot as plt

# backend_bases.FigureCanvas : 图表的绘制画布：图表画布
# backend_bases.Renderer : 在FigureCanvas上如何绘图：渲染器
# artist.Artist : 使用Renderer在FigureCanvas上绘图：艺术家
# FigureCanvas和Renderer需要处理底层的绘图操作
# Artist则处理所有的高层结构
#
# 直接使用Artists创建图表的标准流程如下：
#   创建Figure对象
#   用Figure对象创建一个或者多个Axes或者Subplot对象
#   调用Axes等对象的方法创建各种简单类型的Artists

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot([1, 2, 3], [1, 2, 1])
ax.plot([0, 3], [1, 2])
ax.set_xlabel("x label")


plt.show()
