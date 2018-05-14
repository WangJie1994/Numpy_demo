import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A)

print(np.argmin(A))
print(np.argmax(A))

print(np.mean(A))
print(A.mean())
print(np.average(A))
print(np.median(A)) # 中位数
print(np.cumsum(A)) # 逐个累加
print(np.diff(A)) # 差
print(np.nonzero(A)) # 非零的数
A = np.arange(14, 2, -1).reshape((3, 4))
print(A)
print(np.sort(A, axis=0))
print(np.sort(A, axis=1))

print(np.transpose(A))
print(A.T)
print((A.T).dot(A))

print(np.clip(A, 5, 9))

print(A)
print(np.mean(A, axis=0))
print(np.mean(A, axis=1))