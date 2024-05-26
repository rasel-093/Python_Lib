import matplotlib.pyplot as plt
import numpy as np

team1_score = [20,35,40,25,24,27,50,47,38, 39]
team2_score = [7,22,40,34,25,50,43, 49, 23, 37]

scoreRange = np.arange(0, 50, 5) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
plt.scatter(team1_score, scoreRange, color='r', alpha=0.5)
plt.scatter(team2_score, scoreRange, color='g', alpha= 1)
plt.show()
