#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    last_two = s[-2:]
    hour = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    if(last_two == "PM"):
        if(hour == "12"):
            pass
        else:
            hour = str(int(hour) + 12)
        return "{}:{}:{}".format(hour, minutes, seconds)
    if(last_two == "AM"):
        if(hour == "24" or hour == "12"):
            hour = "00"
        return "{}:{}:{}".format(hour, minutes, seconds)
    else:
        return s[0:len(s)-2]
    
    

if __name__ == '__main__':

    s = ["12:40:22AM", "06:40:03AM", "12:40:22AM", "12:45:54PM"]

    result = timeConversion(s[3])

    print(result)

    
