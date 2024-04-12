import numpy as np

a = np.ones((2, 3))
print("array a:", a)

b = np.zeros((4, 2))
print("array b:", b)

c = np.full((2, 2), 7)
print("array c:", c)

d = np.eye(3)
print("array d:", d)

e = np.diag(np.array([1, 2, 3, 4]))
print("array e:", e)

f = np.arange(10)
print("array f:", f)

g = np.random.randint(10, size=(2, 2))
print("array g:", g)

h = np.random.rand(2, 2)
print("array h:", h)

''' array a: [[1. 1. 1.]
 [1. 1. 1.]]
array b: [[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]
array c: [[7 7]
 [7 7]]
array d: [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
array e: [[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
array f: [0 1 2 3 4 5 6 7 8 9]
array g: [[8 4]
 [9 1]]
array h: [[0.45451176 0.41595986]
 [0.71496855 0.06778916]] '''
