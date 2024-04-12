import numpy as np

a = np.array([1, 2, 3, 4])
b = 5
print("array a:", a)
print("scalar b:", b)
c = a + b
print("array c:", c)

d = np.ones((8, 1, 6, 1))
print("shape of d:", d.shape)
e = np.ones((7, 1, 5)) 
print("shape of e:", e.shape)
f = d + e
print("shape of f:", f.shape)

g = np.array([[1, 2, 3, 4]]).T
h = np.array([[1, 0, 1, 2], [2, 1, 0, 3], [3, 2, 1, 4], [4, 3, 2, 5]])
print("array g:", g)
print("array h:", h)
print("shape of g:", g.shape)
print("shape of h:", h.shape)
i = g * h
print("array i:", i)
print("shape of i:", i.shape)
''' array a: [1 2 3 4]
scalar b: 5
array c: [6 7 8 9]
shape of d: (8, 1, 6, 1)
shape of e: (7, 1, 5)
shape of f: (8, 7, 6, 5)
array g: [[1]
 [2]
 [3]
 [4]]
array h: [[1 0 1 2]
 [2 1 0 3]
 [3 2 1 4]
 [4 3 2 5]]
shape of g: (4, 1)
shape of h: (4, 4)
array i: [[ 1  0  1  2]
 [ 4  2  0  6]
 [ 9  6  3 12]
 [16 12  8 20]]
shape of i: (4, 4) '''
