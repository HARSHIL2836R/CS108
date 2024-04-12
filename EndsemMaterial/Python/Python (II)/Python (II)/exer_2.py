import numpy as np

def distance(arr):
    diff = arr.reshape(arr.shape[0], 1, arr.shape[1]) - arr
    dist = np.sqrt(np.sum(diff**2, axis=2))
    return dist

if __name__ == '__main__':
    arr = np.random.randint(0, 5, size=(5, 2))
    print(arr)
    print(distance(arr))
''' [[0 4]
 [0 1]
 [4 4]
 [4 1]
 [1 3]]
[[0.         3.         4.         5.         1.41421356]
 [3.         0.         5.         4.         2.23606798]
 [4.         5.         0.         3.         3.16227766]
 [5.         4.         3.         0.         3.60555128]
 [1.41421356 2.23606798 3.16227766 3.60555128 0.        ]] '''
