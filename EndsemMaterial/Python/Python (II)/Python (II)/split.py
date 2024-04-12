import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array_split(a, 3)
print("array b:", b)
c  = np.array_split(a, 4)
print("array c:", c)

d = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
e = np.array_split(d, 2)
print("array e:", e)
f = np.array_split(d, 2, axis=1)
print("array f:", f)

g = np.hsplit(d, 2)
print("array g:", g)
h = np.vsplit(d, 3)
print("array h:", h)

''' array b: [array([1, 2]), array([3, 4]), array([5, 6])]
array c: [array([1, 2]), array([3, 4]), array([5]), array([6])]
array e: [array([[1, 2],
       [3, 4],
       [5, 6]]), array([[ 7,  8],
       [ 9, 10],
       [11, 12]])]
array f: [array([[ 1],
       [ 3],
       [ 5],
       [ 7],
       [ 9],
       [11]]), array([[ 2],
       [ 4],
       [ 6],
       [ 8],
       [10],
       [12]])]
array g: [array([[ 1],
       [ 3],
       [ 5],
       [ 7],
       [ 9],
       [11]]), array([[ 2],
       [ 4],
       [ 6],
       [ 8],
       [10],
       [12]])]
array h: [array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])] '''
