import numpy as np

a = np.arange(4)

print(a)

b = a
c = a
d = b

a[0] = 11

print(a)
print(b)
print(b is a)
print(c)
print(d)

d[1:3] = [22, 33]

print(a)

b = a.copy()
a[1] = 100
print(a)
print(b)
