#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # จัดเรียงแต่ละแถว
    grid = [sorted(row) for row in grid]
    
    # ตรวจสอบแต่ละคอลัมน์ว่าถูกเรียงตามลำดับจากบนลงล่างหรือไม่
    for i in range(len(grid[0])):  # ตรวจสอบทุกคอลัมน์
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j-1][i]:
                return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open("gridChallenge.txt", "w") 
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
