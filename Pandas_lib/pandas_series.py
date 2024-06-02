import pandas as pd

# A Pandas Series is like a column in a table.
#
# It is a one-dimensional array holding data of any type.
# list to pandas Series
a = [1, 7, 2]
series = pd.Series(a)
print(series)

# With the index argument, you can name your own labels.
series = pd.Series(a, index=['x', 'y', 'z'])
print(series)
# When you have created labels, you can access an item by referring to the label.
print(series['y'])

# Dictionary to pandas Series
calories = {"day1": 420, "day2": 380, "day3": 390}
series = pd.Series(calories)
# Passing specific index
series = pd.Series(calories, index=['day1', 'day3'])
print(series)