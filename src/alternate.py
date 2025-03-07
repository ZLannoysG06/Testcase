#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    max_length = 0
    for char1 in set(s):
        for char2 in set(s):
            if char1 != char2:
                current_str = ''.join([ch for ch in s if ch == char1 or ch == char2])
                if all(current_str[i] != current_str[i - 1] for i in range(1, len(current_str))):
                    max_length = max(max_length, len(current_str))
    return max_length

if __name__ == '__main__':
    fptr = open("alternate.txt", "w") 

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
