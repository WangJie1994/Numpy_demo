import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

print(np.vstack((A, B))) # 上下合并
print(np.hstack((A, B))) # 左右合并

print(A.reshape(3, 1))
print(A[:, np.newaxis])
A = A[:, np.newaxis]
print(A)
C = np.concatenate((A, A, A), axis=1)
print(C)