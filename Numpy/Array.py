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
# print(arr[4:])
#
# # Slice elements from the beginning to index 4 (not included):
# print(arr[:4])
#
# # Negative slicing
# print(arr[-5:-1])
#
# # Using Step value [start:stop:step]
# print(arr[1:5:2])
# print(arr[::2])  # All from start to end step by 2


# Slicing 2D array
# From both elements, return index 2:
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])
# # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 1:4])

# Array shape
# The shape of an array is the number of elements in each dimension.
# fiveDArray = np.array([1, 2, 3, 4, 5, 6], ndmin=5)
#
# print("Array shape: ", arr.shape)
# print("5D Array shape: ", fiveDArray.shape)


# Array Reshape
# Reshape from 1-D to 2-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12])
# newArr = arr.reshape(4, 3)  # 4 row, 3 column
# print("Array: ", arr)
# print("Reshaped array: ",newArr ) # base of reshape array is original array. so it's view


# Reshape from 1-D to 3-D
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# # Pass -1 as the value, and NumPy will calculate this number for you.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print("Reshaped 3D Array: ", newarr)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print("Any D to 1-D array : ", newarr)



# Iterating array

# Iterating 1-D array
# arr = np.array([1, 2, 3, 4, 5, 6])
# for x in arr:
#     print(x) # will print array element one by one

# Traverse 2D array by 1D array
# twoDArray = np.array([[1, 2, 3], [4, 5, 6]])
# for x in twoDArray:
#     print(x) # x is 1D array here

# Traverse 2D array by each element

# for x in twoDArray:
#     for y in x:
#         print(y)  # Will print each element

# Iterating Arrays Using nditer()

# for x in np.nditer(twoDArray):
#     print(x)
#
# # Iterate through the array as a string:
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:
# for x in np.nditer(twoDArray[:, ::2]):
#     print(x)

# Enumerated Iteration Using ndenumerate()
# for idx, x in np.ndenumerate(twoDArray):  # print value
#     print(idx, x)


# Joining numpyr arrays
# Joining means putting contents of two or more arrays in a single array.

# Both are  1D array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# arr3 = np.array([[1, 2, 3],[4, 5, 6]])
# arr4 = np.array([[4,5,6],[7,8,4]])
# arr_join1 = np.concatenate((arr1, arr2))
# arr_join3 = np.concatenate((arr3,arr4))
# print('Both are 1D array: ', arr_join1)
# print('Both are 2D', arr_join3)

# Join two 2-D arrays along rows (axis=1):
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference
# is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis
# which would result in putting them one over the other,
# arr = np.stack((arr1, arr2), axis=0)
# print(arr)

# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
# arr = np.hstack((arr1, arr2))
# print(arr)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
# arr = np.vstack((arr1,arr2))
# print(arr)

# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
# arr = np.dstack((arr1,arr2))
# print(arr.ndim)
# print(arr)



# Numpy Array Splitting
# arr = np.array([1,2,3,4,5,6])
# newArr = np.array_split(arr, 3)
# print(newArr[2])

# If the array has less elements than required, it will adjust from the end accordingly.
# newarr = np.array_split(arr, 4)
# print(newarr)


# # Split the 2-D array into three 2-D arrays
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)

# # Split the 2-D array into three 2-D arrays along rows.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newArr = np.array_split(arr, 3, axis=0)
# print(newArr)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newArr = np.hsplit(arr, 3)
# newArrVSplit = np.vsplit(arr,3)
# print(newArrVSplit)

# v vplist cuts vertical arrangement , hsplit cuts horizontal arrangement










## NumPy Searching Arrays
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)  # Returns index of searched value
# print(x)

# Find the indexes where the values are even:
# evenArray = np.where(arr%2 == 0)
# print(evenArray)


# There is a method called searchsorted() which performs a binary search
# in the array, and returns the index where the specified value would be inserted
# to maintain the search order.

# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 8, side='right')  # This function is not inserting, just saying where to insert
# print(x)


# To search for more than one value, use an array with the specified values.
# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6])
# print(x)


# NumPy Sorting Arrays
# arr = np.array([3, 2, 0, 1])
# sorted_array = np.sort(arr)
# print(sorted_array)
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))
#
# arr = np.array([True, False, True])
# print(np.sort(arr))
#
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))









# NumPy Filter Array

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newArr = arr[x]
# print(newArr)  # Prints only true equivalent index of the arr


# Create a filter array that will return only values higher than 42:(Dynamic)
# arr = np.array([41, 42, 43, 44])
# filter_array = []
# for val in arr:
#     if val>42:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)
#
# filterd_array = arr[filter_array]
# print(filterd_array)

# Create a filter array that will return only even elements from the original array:
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# even_filter = []
# for val in arr:
#     if val % 2 == 0:
#         even_filter.append(True)
#     else:
#         even_filter.append(False)
# even_array = arr[even_filter]
# print(even_array)

# Creating Filter Directly From Array

# Create a filter array that will return only values higher than 42:
# arr = np.array([41, 42, 43, 44])
# filtered_array = arr > 42
# print(filtered_array)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# even_filter = arr % 2 == 0
print(arr[arr % 2 == 0])




