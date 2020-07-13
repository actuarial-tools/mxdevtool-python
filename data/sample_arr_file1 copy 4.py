import os
import sys
import numpy as np
import pickle

#arr = np.array(range(0,10300000))
arr = np.random.randn(10000000,40)

print(len(arr))
print(arr)
print(arr[1])
print(arr[2:5])
print(arr[::1])
print(arr.dtype)

np.save('large_file', arr)