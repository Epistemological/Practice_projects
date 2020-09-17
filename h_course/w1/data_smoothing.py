import random

# Exercise 3a
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean = []
    for i in range(n):
        temp = x[i: i+width]
        sum_ = 0
        for elm in temp:
            sum_+= elm
        mean.append((sum_ / width))
    return mean
x = [0,10,5,3,1,5]
print(sum(moving_window_average(x, 1)))

# Exercise 3b
R = 1000
random.seed(1)
x = []
for i in range(R):
    num = random.uniform(0,1)
    x.append(num)
Y = []
Y.append(x)

for i in range(10):
    mov_avg = moving_window_average(x, n_neighbors=5)
    Y.append(mov_avg)
print(Y[5][9])

# 3b alt. solution
random.seed(1)
x = [random.random() for i in range(R)]
Y = [x] + [moving_window_average(x, 5) for i in range(1,10)]
print(Y[5][9])

ranges = []

for i in Y:
    calc = max(i) - min(i)
    ranges.append(calc)
print(ranges)








