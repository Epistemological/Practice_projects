import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    removers = []
    for i in arr:
        removers.append(i)
    new_arr = [sum(arr) - removers[0],
               sum(arr) - removers[1],
               sum(arr) - removers[2],
               sum(arr) - removers[3],
               sum(arr) - removers[4],
               ]
    return print(*[min(new_arr), max(new_arr)])




if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)