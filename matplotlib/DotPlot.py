import matplotlib.pyplot as plt
import numpy as np

a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
x1 = np.array([1, 2, 3, 4])
y1 = np.array([1, 4, 9, 16])
x2 = x1
y2 = np.array([1, 8, 27, 64])
t = np.arange(0, 5, .2)

# print(t)
#plt.plot(a, b, ':') #Plots dot
plt.plot(y1, 'o:r') #dotted line with red marker
# plt.plot(a, b, marker='D') #Plots line with dot
# Plots red dashes, blue squares and green triangles
# plt.plot(t, t,'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.plot(np.array(a), np.array(b), marker='o', linestyle=':', linewidth='5', ms=10, mec='g', mfc='r')
# multiple line in same plot function
# plt.plot(x1, y1, x2, y2, linewidth='5', linestyle=':')
# marker = marker type, ms = marker size, mec = marker color(r,g,b,c,m,y,k,2)
# mfc = marker face color,
# marker = 'o', '*','x'
# plt.axis((0, 10, 0, 25))
# axis(xmin,xmax,ymin,ymax)
plt.show()
