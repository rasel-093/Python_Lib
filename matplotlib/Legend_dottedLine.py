import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]

# Create plots
fig = plt.figure()
ax = plt.subplot()

# Dotted line
# ax.plot(a, b, 'k--')
# ax.plot(a, c, 'k:')

# Continues line having different color
ax.plot(a, b)
ax.plot(a, c)

# Create the legend
legend = ax.legend(["Frequency", "Periods"], loc="lower right", fontsize='medium')

# Set bg color of legend
legend.get_frame().set_facecolor('yellow')

# title
plt.title("Frequency of a signal")
# Display the figure
plt.show()
