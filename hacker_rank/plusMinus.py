import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positives += 1
        else:
            negatives += 1

    pos_rat = positives / n
    pos_form = f"{pos_rat:.6f}"

    neg_rat = negatives / n
    neg_form = f"{neg_rat:.6f}"

    zer_rat = zeros / n
    zer_form = f"{zer_rat:.6f}"

    return print(pos_form + '\n' + neg_form + '\n' + zer_form)





if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)