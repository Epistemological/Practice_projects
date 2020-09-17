import math
import random

print(math.pi / 4)


random.seed(1) # Fixes the seed of the random number generator.

def rand():
    random_nr = random.uniform(-1, 1)
    return random_nr

n = range(3)

for x in n:
    R = rand()
print(R)


