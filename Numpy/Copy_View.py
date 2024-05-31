import numpy as np

# The main difference between a copy and a view of an array is that
# the copy is a new array, and the view is just a view of the original array.
# any changes made to the copy will not affect original array
# any changes made to the original array will not affect the copy.
# any changes made to the view will affect the original array,
# and any changes made to the original array will affect the view.

# Copy
arr = np.array([1,2,3,4,5,6,7,8,9,10])
newArrCopy = arr.copy()
arr[0] = 40
print("Array : ", arr)
print("New Array-copy: ", newArrCopy)

# View
newArrView = arr.view()
arr[1] = 50
print("Array : ", arr)
print("New Array-View : ", newArrView)
newArrView[3] = 60
print("Array: ", arr)

#  NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

print("Base of newArrCopy : ", newArrCopy.base)
print("Base of newArrView : ", newArrView.base)
