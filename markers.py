# use the keyword argument marker to emphasize each point with a specified marker

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2,5, 6, 7, 8])
# plt.plot(ypoints, marker='o')
# plt.plot(ypoints, marker='*')
# plt.plot(ypoints, marker='s')

#format strings fmt   marker|line|color
# plt.plot(ypoints, 'o:r')
# plt.plot(ypoints, 'o-g')
# plt.plot(ypoints, 's--b')
# plt.plot(ypoints, 's-.m')
plt.plot(ypoints, 'o--g', ms=20, mec='r', mfc='b')  #marker size, markerEdgeColor, markerFaceColor

plt.show()
