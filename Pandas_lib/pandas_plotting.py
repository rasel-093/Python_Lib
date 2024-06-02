import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data_without_date.csv')
# df.plot()
# plt.xlabel('Attribute-name')
# plt.ylabel('Attribute-Value')
# plt.show()

# Scatter plot
# Duration and calories have a good relationship
# The values are less scattered
# df.plot(kind='scatter', x='Duration', y='Calories')
# plt.show()

# Duration and Maxpulse has a bad relationship
# The values are much scattered
# df.plot(kind='scatter', x='Duration', y='Maxpulse')
# plt.show()


# Histogram
df['Duration'].plot(kind='hist')
plt.show()