import math
import os
import random
import re
import sys

def hourglass_sum(arr):
    """Calculates the maximum hourglass sum in a 6x6 array.

    Args:
        arr: A 6x6 list of integers.

    Returns:
        The maximum hourglass sum.
    """

    max_sum = -63  # Initialize with minimum possible sum
    
    for i in range(4):
        for j in range(4):
            hourglass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            max_sum = max(max_sum, hourglass_sum)

    return max_sum

if __name__ == '__main__':
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)
    print(result)

