import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))

x = np.arange(0.0, 5.01, 0.01)

plt.plot(x, np.log(1 + np.exp(x)), label="$y=ln(1+e^x)$", color="r", linewidth=1)
plt.plot(x, x, "b--", label="$y=x$", color="g", linewidth=1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("y=ln(1+exp{x})")
# 显示图示
plt.legend()
plt.savefig("./fig1.png")
plt.show()
