import numpy as np

a = np.array(1)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Only element of a:", a)
print("2nd element of b:", b[1])
print("3rd element of 2nd row of c:", c[1, 2])
print("2nd element of 1st row of 2nd array of d:", d[1, 0, 1])

print("First 4 elements of b:", b[:4])
print("Last 2 elements of b:", b[-2:])
print("Middle 3 elements of b:", b[1:4])
print("Every even index element of b:", b[::2])
print("Every element of odd row and even column of c:", c[1::2, ::2])
'''
Only element of a: 1
2nd element of b: 2
3rd element of 2nd row of c: 6
2nd element of 1st row of 2nd array of d: 8
First 4 elements of b: [1 2 3 4]
Last 2 elements of b: [4 5]
Middle 3 elements of b: [2 3 4]
Every even index element of b: [1 3 5]
Every element of odd row and even column of c: [[ 4  6]
 [10 12]]
'''