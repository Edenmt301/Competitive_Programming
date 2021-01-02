#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b, n):
    valid=True
    for i in bill:
        if i<0 or i>10**4:
            valid=False
    if (n<2 or n>10**5) or (k<0 or k>n) or valid==False:
        return()
    n=len(bill)
    sum=0
    for i in range(n):
        if i==k:
            continue
        else:
            sum += bill[i]
    bActual=sum/2
    if bActual<b:
        print(int(b-bActual))
    elif bActual==b:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b, n)
