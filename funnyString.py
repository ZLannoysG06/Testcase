#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    n = len(s)
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[n - i]) - ord(s[n - i - 1])):
            return "Not Funny"
    return "Funny"



if __name__ == '__main__':
    fptr = open("funnyString.txt", "w") 

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
