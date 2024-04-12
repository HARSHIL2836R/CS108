import numpy as np

a = np.array(1)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Dim of a:", a.ndim)
print("Dim of b:", b.ndim)
print("Dim of c:", c.ndim)
print("Dim of d:", d.ndim)

e = np.array([[1, 2], [3, 4]], ndmin=5)
f = np.array([[[1], [2]], [[3], [4]], [[5], [6]]], ndmin=2)

print("Array e:", e)
print("Dim of e:", e.ndim)

print("Array f:", f)
print("Dim of f:", f.ndim)
''' Dim of a: 0
Dim of b: 1
Dim of c: 2
Dim of d: 3
Array e: [[[[[1 2]
    [3 4]]]]]
Dim of e: 5
Array f: [[[1]
  [2]]

 [[3]
  [4]]

 [[5]
  [6]]]
Dim of f: 3 '''
