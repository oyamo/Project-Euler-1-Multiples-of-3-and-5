
#you can change the output from stdin to print()
import sys
import os

def find_sum(arr):
    result = []
    for no in arr:
        l3 = 0
        l5 = 0
        for n in range(no-1,0,-1):
            if(n%3==0):
                l3 = n
                break
        for n in range(no-1,0,-1):
            if(n%5==0):
                l5 = n
                break
        n3 = (l3-(3-3))//3
        list3 = set([3+((c-1)*3) for c in range(n3+1) ])
        n5 = (l5-(5-5))//5
        list5 = set([5+((c-1)*5) for c in range(n5+1) ])
        final_set = list(list3 | list5)
        SUM = sum(final_set)
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
