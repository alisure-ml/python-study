import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(221, facecolor='r')
ax.set_title("PCA")

ax = fig.add_subplot(222, facecolor='g')
ax.set_title("PCA")

ax = fig.add_subplot(223, facecolor='b')
ax.set_title("PCA")

ax = fig.add_subplot(224, projection='polar')
ax.set_title("PCA")

plt.show()
