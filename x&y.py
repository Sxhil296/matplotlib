# plot() function is used to draw points (markers) in a diagram.
#it draws a line from point to point


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

#plotting without line
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

#multiple points
# x1points=np.array([1, 2, 6, 8])
# y1points=np.array([3, 8, 1 ,10])
#
# plt.plot(x1points, y1points, 'o')
# plt.show()


#default x-points
y2points=np.array([3, 8, 1, 10, 5, 7])
plt.plot(y2points)
plt.show()