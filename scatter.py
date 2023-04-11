# you can use the scatter() function to draw a scatter plot.
# The scatter() function plots one dot for each observation.
# It needs two arrays of the same length,
# one for the values of the x-axis, and one for values on the y-axis:


import matplotlib.pyplot as plt
import numpy as np

# day one, the age and the speed of 13 cars
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# plt.scatter(x, y, color='hotpink')

# color each dot
# colors = np.array(
#     ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
#      "magenta"])
colors=np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()

# day two, the age and the speed of 15 cars
# x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
# y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
# plt.scatter(x, y, color='#88c999')

plt.show()
