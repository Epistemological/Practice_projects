import numpy as np

#print(np.linspace(0,100,10))
#print(np.logspace(1, 2, 10)
#print(np.logspace(np.log10(250), np.log10(500), 10))

X = np.array([[1,2,3], [4,5,6]])
#print(X.size)

x = np.random.random(10)

#print(np.any(x > 0.9))
#print(np.all(x >= 0.1))
#print(x)

x = 20
print(not np.any([x%i == 0 for i in range(2,x)]))