import math
import random

x = (1,1)
y = (0,0)

#2a
print(math.pi / 4)

#2b
random.seed(1)
def rand():
    return random.uniform(-1,1)
print(rand())

#2c
def distance(x, y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )
print(distance((0,0),(1,1)))

#2d
def in_circle(x, origin = [0,0]):
    return distance(x, origin) < 1
print(in_circle((1,1)))

# 2e solution 1
R = 10000
x = [ (rand(), rand()) for i in range(R) ]
inside = [ in_circle(p) for p in x ]
print(sum(inside) / R)

# 2e solution 2
T = 10000
z = []
inside2 = []
for i in range(T):
    point = [rand(), rand()]
    z.append(point)
for j in z:
    inside2 = [in_circle(j)]
print(sum(inside) / T)

#2f

print( (math.pi / 4) - (sum(inside)/T)  )

















