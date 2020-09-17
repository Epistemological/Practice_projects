import matplotlib.pyplot as plt
import numpy as np

#plt.plot([0,1,2,3,4])
x = np.logspace(-1,1,40)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x,y1, "bs-", linewidth=2, markersize=4, label="First")
plt.loglog(x,y2, "gs-", linewidth=2, markersize=4, label="Second")
plt.legend(loc="upper left")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.savefig("testplot.pdf")
plt.show()





