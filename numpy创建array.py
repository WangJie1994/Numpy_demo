import numpy as np

a = np.array([2, 23, 4], dtype=np.int)
print(a)
print(a.dtype)

b = np.array([[2, 3, 4],
              [5, 6, 7]])
print(b)

c = np.zeros((3, 4))
print(c)
print(c.shape)

d = np.ones((3, 4), dtype=np.int)
print(d)

e = np.empty((2, 3))
print(e)

f = np.arange(10, 20, 2)
print(f)

g = np.arange(12).reshape(3,4)
print(g)

h = np.linspace(1, 10, 20)
print(h)