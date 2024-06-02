import pandas as pd

# head() method returns the headers and a specified number of rows, starting from the top.
# if the number of rows is not specified, the head() method will return the top 5 rows.
df = pd.read_csv('data.csv')
# print(df.head(10))
# print(df.tail(10))


# info(), that gives you more information about the data set.
# print(df.info())

# Data cleaning
# Data cleaning means fixing bad data in your data set.
#
# Bad data could be:
#
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

#  Cleaning Empty Cells and NULL valued cell:
# new_df = df.dropna()  # If you want to change the original DataFrame, use the inplace = True argument:
# print(new_df.info())
# Remove all rows with NULL values:
# df.dropna(inplace=True)

# The fillna() method allows us to replace empty cells with a value:
# df.fillna(130, inplace=True)
# print(df.info())

# To only replace empty values for one column,
# specify the column name for the DataFrame:
# df["Calories"].fillna(130, inplace=True)
# print(df.info())

# A common way to replace empty cells,
# is to calculate the mean, median or mode value of the column.
# mean = df['Calories'].mean()
# median = df['Calories'].median()
# mode = df['Calories'].mode()
# df['Calories'].fillna(mean)
# df['Calories'].fillna(median)
# print(mean)
# df['Calories'].fillna(mean, inplace=True)
# print(df.info())



# Cleaning Data of Wrong Format(Nan/ 20240522 etc)
# Not working
# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)
# print(df.to_string())


# Fixing Wrong Data
#  like if someone registered "199" instead of "1.99".
# Fixing 7 no record manually
# df.loc[7, 'Duration'] = 45
# print(df)

# Replacing value using loop
# for x in df['Duration'].index:
#     if df['Duration'].loc[x] > 120:
#         df.loc[x, 'Duration'] = 120
#         #df.loc[x, "Duration"] > 120:
#     # print(x, df['Duration'].loc[x])
#
# print(df)

# Delete rows where "Duration" is higher than 120:
# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.drop(x, inplace=True)
#
# print(df)







# Removing duplicates
# Will return true for duplicated index
print(df.duplicated()) # Appeared before the return index

df.drop_duplicates(inplace=True)
print(df)
