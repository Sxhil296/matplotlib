import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
labels=["Apples", "Bananas", "Cherries", "Dates"]
explodes=[0.1, 0, 0, 0]
colors = ["black", "hotpink", "b", "#4CAF50"]


#The explode parameter, if specified, and not None, must be an array with one value for each wedge.
plt.pie(y, labels=labels, startangle=90, explode=explodes, shadow=True, colors=colors)
plt.legend(title="Four Fruits") #list of explanation for each wedge
plt.show()