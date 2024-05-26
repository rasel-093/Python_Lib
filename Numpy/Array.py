import numpy as np
list = [2, 3, 9, 23, 4, 5, 6, 2, 7]
dict = {2, 3, 45, 6, 7, 7, 93, 2}
tuple = (2,4,6,9,5,2,4,3)
# 1D array
listToArray = np.array(list)
dictToArray = np.array(dict)
tupleToArray = np.array(tuple)

# 2D array
twoDArray = np.array([[1,2,3],[4,5,6]])
# 3D array using 2D array
threeDArray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(threeDArray)

# Check number of dimension
# print(twoDArray.ndim)
# print(threeDArray.ndim)

# n dimensional array
ndimArr = np.array([1, 2, 3, 4], ndmin=5)
# print(ndimArr.ndim)

# Array accessing
# print(listToArray[0])
# print(twoDArray[0, 1])
# print(threeDArray[0, 1, 2])

# Print the 2nd last element from the second dim
# print(twoDArray[1,-2])

# Slicing array
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])
# includes the start index, but excludes the end index.

# Slice elements from index 4 to the end of the array:
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

# Negative slicing
print(arr[-5:-1])

# Using Step value [start:stop:step]
print(arr[1:5:2])
print(arr[::2])  # All from start to end step by 2


# Slicing 2D array
# From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
