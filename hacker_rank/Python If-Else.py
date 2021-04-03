import math
import os
import random
import re
import sys

def weird_func(n):
    mod = n % 2

    if mod > 0:
        return print('Weird')
    elif mod == 0 and n >= 2 and n <= 5:
        return print('Not Weird')
    elif mod == 0 and n >= 6 and n <= 20:
        return print('Weird')
    elif mod == 0 and n > 20:
        return print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())