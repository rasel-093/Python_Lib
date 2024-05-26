import matplotlib.pyplot as plt
import numpy as np


# x and y coordinates data
student = np.array(["Rasel", "Shezan", "Tanzid", "Shoikot", "Toufique", "Niloy"])
marks = np.array([85, 56, 99, 77, 69, 89])
myexplode = [0.2, 0, 0, 0, 0, 0]
# Plot a bar graph
plt.pie(marks, labels=student, autopct='%1.2f%%', explode=myexplode)
plt.legend(title="Four Fruits:")
plt.title("Student vs marks")
plt.show()
