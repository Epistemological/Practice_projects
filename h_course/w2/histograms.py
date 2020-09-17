import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)

plt.hist(x, normed=True, bins=np.linspace(-5, 5, 21))
plt.show()

x = np.random.gamma(2,3,100000)
plt.hist(x, bins=30, cumulative=True, normed=False, histtype="step", color="blue")
plt.show()

plt.subplot(333)
plt.show()