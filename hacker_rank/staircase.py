import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    print(*[''.join(' '*i + '#'*(n-i)) for i in range(n, -1, -1)][1:], sep='\n')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
