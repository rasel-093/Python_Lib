# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np

# arr = np.array([1, 2, 3, 4])
# arrStr = np.array(['apple', 'banana', 'cherry'])
# print(type(arr))  # Prints the data type of an array object
# print(arrStr.dtype)

# We use the array() function to create arrays, this function
# can take an optional argument: dtype that allows us to define the expected data type of the array elements:
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr.dtype)
# For i, u, f, S and U we can define size as well.

# Create an array with data type 4 bytes integer:
# arr = np.array([1,2,3,4,5,6], dtype='i4')
# print(arr.dtype)

# ValueError: In Python ValueError is raised when the
# type of passed argument to a function is unexpected/incorrect.

# A non integer string like 'a' can not be converted to integer (will raise an error):
# arr = np.array(['a', '2', '3'], dtype='i') # will thorow error
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
#The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
# arr = np.array([1.1, 2.1, 3.1])
# newArr = arr.astype('i')
# print(newArr)
# print(newArr.dtype)
# Change data type from float to integer by using int as parameter value:
# newArr = arr.astype(float)
# print(newArr)
# print(newArr.dtype)

# Change data type from integer to boolean
arr = np.array([1, 0, 3])
newArr = arr.astype(bool)
print(arr)
print(newArr.dtype)