import numpy as np
times=[5.0,2.30,3.0,5.10]
distances=[20,35,10,5]
times=np.array(times)
distances=np.array(distances)

print(distances/times)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
