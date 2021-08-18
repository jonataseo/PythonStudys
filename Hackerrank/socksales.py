#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    socks_to_str = list(map(str, ar))
    soluction_dir = {}
    for sock in socks_to_str:
        if sock in soluction_dir:
            soluction_dir[sock] += 1
        else:
            soluction_dir[sock] = 1
    number_of_pairs = 0
    print(soluction_dir)
    for possible_pairs in soluction_dir:
        if (soluction_dir[possible_pairs] / 2) > 0:
            number_of_pairs += 1 * math.floor((soluction_dir[possible_pairs] / 2))
    return number_of_pairs

if __name__ == '__main__':
    
    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    print(result)
