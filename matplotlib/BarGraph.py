import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x and y coordinates data
student = np.array(["Rasel", "Shezan", "Tanzid", "Shoikot", "Toufique", "Niloy"])
marks = np.array([85, 56, 99, 77, 69, 89])

# Plot a bar graph
# Vertical bar
plt.bar(student, marks, width=0.1)
#horizontal bar
# plt.barh(student,marks)
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student vs marks")
plt.show()
