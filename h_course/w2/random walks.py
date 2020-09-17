import random
import numpy as np
import matplotlib.pyplot as plt


x_0 = np.array([[0], [0]])
delta_x = np.random.normal(0,1, (2,10000))
x = np.concatenate((x_0, np.cumsum(delta_x, axis = 1)), axis=1)
plt.plot(x[0], x[1], "ro-")
plt.savefig("rw2.pdf")
plt.show()