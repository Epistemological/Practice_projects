import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0,1,10)
y = x**2
plt.loglog(x,y,"bo-")
plt.show()
