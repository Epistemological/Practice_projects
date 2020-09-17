import numpy as np

zero_vector = np.zeros(5)
zero_matrix = np.zeros((5, 3))
zero_matrix

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
[[1, 3], [5, 9]]
np.array([[1, 3], [5, 9]])

A = np.array([[1, 3], [5, 9]])
A.transpose()

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[2, 4, 6], [8, 10, 12]])
x[0:2]

z = x + y
z
X[:, 1]
Y[:, 1]

Z = X[:, 1] + Y[:, 1]
Z
X[1, :]

r = np.array([1, 2])
d = np.array([1, 2, 3])

###  Indexing NumPy Arrays

z1 = np.array([1, 2, 3, 4, 5, 6])
z2 = z1 + 1
(z1)
(z2)

ind = [0, 2, 3]  # list index of array
ind = np.array([0, 2, 3])  # array index of array
z1 < 6
z2[z1 < 6]
ind = z1 < 6
(ind)

u = np.array([1, 2, 3, 4])
w = u[0:3]
# print(w)
# w[0] = 3
# print(w)
# print(u)

a = np.array([1, 3, 5, 7])
ind = np.array([0, 1, 3])
w = a[ind]
w[0] = 3
print(w)
print(ind)

