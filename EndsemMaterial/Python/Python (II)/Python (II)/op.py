import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [1, 2]])
print("array a:", a)
print("array b:", b)
c = a + b
print("array c:", c)
d = a - b
print("array d:", d)
e = a * b
print("array e:", e)
f = a / b
print("array f:", f)
g = a ** b
print("array g:", g)
h = a % b
print("array h:", h)
i = a // b
print("array i:", i)
''' array a: [[1 2]
 [3 4]]
array b: [[5 6]
 [1 2]]
array c: [[6 8]
 [4 6]]
array d: [[-4 -4]
 [ 2  2]]
array e: [[ 5 12]
 [ 3  8]]
array f: [[0.2        0.33333333]
 [3.         2.        ]]
array g: [[ 1 64]
 [ 3 16]]
array h: [[1 2]
 [0 0]]
array i: [[0 0]
 [3 2]] '''
