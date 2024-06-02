import numpy as np
import matplotlib.pyplot as plt

marks = np.array([10,15,17, 18, 20,25,21,24,23,20, 30, 33, 37, 50, 100, 95,  80,80,85, 45,60, 76, 85, 50])
plt.hist(marks, bins=[0, 20, 40, 60, 80, 100])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Student-Marks histogram")
plt.show()
