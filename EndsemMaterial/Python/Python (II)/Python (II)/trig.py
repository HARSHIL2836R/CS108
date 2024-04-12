import numpy as np

a = np.array([[0, np.pi/6], [np.pi/4, np.pi/3]])
print("array a:", a)
b = np.sin(a)
print("array b:", b)
c = np.cos(a)
print("array c:", c)
d = np.tan(a)
print("array d:", d)

e = np.array([[0, 30], [45, 60]])
print("array e:", e)
f = np.radians(e)
print("array f:", f)
g = np.degrees(f)
print("array g:", g)

''' array a: [[0.         0.52359878]
 [0.78539816 1.04719755]]
array b: [[0.         0.5       ]
 [0.70710678 0.8660254 ]]
array c: [[1.         0.8660254 ]
 [0.70710678 0.5       ]]
array d: [[0.         0.57735027]
 [1.         1.73205081]]
array e: [[ 0 30]
 [45 60]]
array f: [[0.         0.52359878]
 [0.78539816 1.04719755]]
array g: [[ 0. 30.]
 [45. 60.]] '''
