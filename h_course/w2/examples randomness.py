import random
import matplotlib.pyplot as plt
import numpy as np

#random.choice([1, 2, 3, 4, 5, 5, 6])

#rolls = []
#for k in range(1000000):
#   rolls.append(random.choice([1, 2, 3, 4, 5, 6]))

#plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7));
#plt.show()

ys = []
for rep in range(10000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)

#plt.hist(ys)
#plt.show()


print(list((1,2,3,4)))