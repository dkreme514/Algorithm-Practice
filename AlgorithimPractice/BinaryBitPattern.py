#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'binary_pattern' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING s as parameter.
#
def binary_pattern(s):
    ans = []
    q = []
    q.append(s)
    size = len(s)
    while (len(q) > 0):
        s = q[0]

        try:
            index = s.index('?')
        except ValueError:
            index = -1

        if (index != -1):

            s1 = s.replace('?', '0', 1)
            q.append(s1)

            s2 = s.replace('?', '1', 1)
            q.append(s2)
        else:
            ans.append(s)

        q.pop(0)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = binary_pattern(s)

    fptr.write(' '.join(result))
    fptr.write('\n')

    fptr.close()