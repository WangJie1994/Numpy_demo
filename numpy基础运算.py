import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a+b)
print(b**2)
print(10*np.sin(a))
print(b<3)
print(b==3)

c = np.array([[1, 1],
              [0, 1]])

d = np.arange(4).reshape((2, 2))
print(c)
print(d)

print(c*d)
print(np.dot(c, d))
print(c.dot(d))


e = np.random.random((2, 4))
print(e)
print(np.sum(e))
print(np.max(e))
print(np.max(e, axis=0))
print(np.max(e, axis=1))
