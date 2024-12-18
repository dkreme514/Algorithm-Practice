#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'remove_duplicates' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def remove_duplicates(s):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = remove_duplicates(s)

    fptr.write(result + '\n')

    fptr.close()