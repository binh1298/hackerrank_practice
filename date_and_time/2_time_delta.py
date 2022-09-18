#!/bin/python3

from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.


def time_delta(t1, t2):
    inputFormat = "%a %d %b %Y %H:%M:%S %z"
    dateTime1, dateTime2 = datetime.strptime(
        t1, inputFormat), datetime.strptime(t2, inputFormat)
    return f"{int(abs(dateTime1.timestamp() - dateTime2.timestamp()))}"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    standard_input = """3
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0700
Sat 02 May 2015 19:54:36 -0700"""
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
    #     fptr.write(delta + '\n')

    # fptr.close()
