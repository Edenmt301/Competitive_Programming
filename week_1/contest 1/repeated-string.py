#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if (n<1 or n>10**12) or (len(s)<1 or len(s)>100):
        return()
    count=0
    subString=''
    allA=True
    for i in s:
        if i not in 'a':
            allA=False
    if allA==True:
        return(n)
    if n%len(s)==0:
        for each in s:
            if each=='a':
                count+=1
        return(count*(n//len(s)))
    else:
        rem=n%len(s)
        for each in s:
            if each=='a':
                count+=1
        extra=0
        for k in range(rem):
            if s[k]=='a':
                extra +=1
        return(count*(n//len(s))+extra)       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
