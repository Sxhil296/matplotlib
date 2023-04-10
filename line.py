import matplotlib.pyplot as plt
import numpy as np

y1=np.array([3, 8, 1, 10])
y2=np.array([6, 2, 8, 11])

# plt.plot(y1, linestyle='dotted', color='r', marker='o')
plt.plot(y1, ls='-', c='r', linewidth='20', marker='o')
plt.plot(y2)
plt.show()
