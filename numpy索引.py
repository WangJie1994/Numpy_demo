import numpy as np

A = np.arange(3, 15)
print(A)

print(A[3])

A = A.reshape((3, 4))
print(A)
print(A[2])
print(A[2][1])
print(A[2, 1])
print(A[2, :])
print(A[:, 1])
print(A[1, 1:3])

for row in A:
    print(row)

for col in A.T: # 对列迭代
    print(col)

for item in A.flat: # A.flat: 迭代器
    print(item)     # A.flatten: 展开的结果