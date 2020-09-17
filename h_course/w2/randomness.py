import random

x = random.choice(range(1,7))
#print(random.choice(random.choice([range(1,7), range(1,9), range(1,11)])))
#print(random.choice(list([1,2,3,4])))

print(sum(random.choice(range(10)) for i in range(10)))

