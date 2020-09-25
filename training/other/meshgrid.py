import matplotlib.pyplot as plt
import numpy as np

#u = np.linspace(-2, 2, 41)
#v = np.linspace(-1, 1, 21)

#X, Y = np.meshgrid(u, v)

#Z = np.sin(3*np.sqrt((X**2 + Y**2)))

#plt.pcolor(Z)
#plt.show()
#plt.savefig('mesh_color.png')

A = np.array([[-1, 1, 2], [-1, 1, 2], [-1, 1, 2]])
plt.pcolor(A, cmap='Blues')
plt.colorbar()
plt.show()