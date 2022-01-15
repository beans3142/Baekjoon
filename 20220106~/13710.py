from sys import stdin
from collections import deque
input=stdin.readline

def bi(n):
    idx=0
    s=[0]*31
    while n:
        s[idx]=n%2
        n>>=1
        idx+=1
    return s

def rep(arr):
    val=0
    idx=0
    while idx<len(arr):
        val+=arr[idx]*(2**idx)
        idx+=1
    return val

N=int(input())
arr=list(map(int,input().split()))


s=bi(arr[0])

for i in range(1,len(arr)):
    now=bi(arr[i])
    for j in range(31):
        s[j]+=abs(((2**j)*now[j]*2**(i-1))-s[j])
    print(s)
    
    '''
    for j in range(31):
        s[j]+=now[j]
'''
