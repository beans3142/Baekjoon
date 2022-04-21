from sys import stdin
from functools import cmp_to_key
input=stdin.readline

def cmp(x,y):
    if int(x+y)<int(y+x):
        return 1
    return -1

n=int(input())
arr=sorted(input().rstrip().split(),key=cmp_to_key(cmp))
print(int(''.join(arr)))
