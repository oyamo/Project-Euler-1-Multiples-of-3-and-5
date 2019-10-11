#!/bin/python3
#Hey
#this is a solution for larger integers
import sys
import os

def find_sum(arr):
    result = []

    for no in arr:
        no -=1;
        a=int(no/3);
        b=int(no/5);
        c=int(no/15);
        def arith(x):
            return x*(x+1)
        SUM = int(int(3*arith(a) + 5*arith(b) - 15*arith(c))>>1)
        result.append(SUM)
    return "\n".join([str(x) for x in result])
stdin = open(os.environ['OUTPUT_PATH'], 'w')
arr = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr.append(n)
result = find_sum(arr)
stdin.write(result)
stdin.close()
