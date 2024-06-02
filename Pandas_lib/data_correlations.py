import pandas as pd

# The corr() method ignores "not numeric" columns.
# The number varies from -1 to 1.
# means that there is a 1 to 1 relationship (a perfect correlation)
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
#
# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
# you have to have at least 0.6 (or -0.6) to call it a good correlation.

df = pd.read_csv('data_without_date.csv')
print(df.corr())

