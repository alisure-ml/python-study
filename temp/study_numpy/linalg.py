import numpy as np
# linalg=linexr+xlgebrx 线性代数

x = [[1, 2], [2, 5]]
y = [3, 7]
# 估计线性模型中的系数 y = a * x
a, residuals, rank, s = np.linalg.lstsq(x, y)
print(a)
print(residuals)
print(rank)
print(s)
# 解形如AX=b的线性方程组
a = np.linalg.solve(x, y)
print(a)
# 矩阵求逆
b = np.linalg.inv(x)
print(b)
# 矩阵广义逆
b = np.linalg.pinv(x)
print(b)
# 矩阵求行列式（标量）
b = np.linalg.det(x)
print(b)
# 矩阵求特征值
b = np.linalg.eigvals(x)
print(b)
# 矩阵求特征值和特征向量
w, v = np.linalg.eig(x)
print(w)
print(v)
# cholesky分解
b = np.linalg.cholesky(x)
print(b)
# svd分解
u, s, v = np.linalg.svd(x)
print(u)
print(s)
print(v)

# norm表示范数
b = np.linalg.norm(x, ord=2)
print(b)
b = np.linalg.norm(x, ord=2, axis=0)
print(b)
b = np.linalg.norm(x, ord=2, axis=1)
print(b)
b = np.linalg.norm(x, ord=2, keepdims=True)
print(b)
