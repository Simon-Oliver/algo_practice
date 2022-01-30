import math
import random
import re
import sys

arr = [1,1,0,-1,-1]

def plusMinus(arr):
    res = {
    "minus":0,
    "plus":0,
    "zero":0
    }

    arr_length = len(arr)

    for e in arr:
        if e > 0:
            res["plus"] += 1
        elif e < 0:
            res["minus"] += 1
        else:
            res["zero"] += 1

    for key,value in res.items():
        print(format(value/len(arr),'.6f'))


plusMinus(arr)
