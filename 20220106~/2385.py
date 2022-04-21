from sys import stdin
from functools import cmp_to_key
from copy import deepcopy
input=stdin.readline

inf = float('inf')

def cmp(x,y):
    if int(x+y)>int(y+x):
        return True
    return False

def cmp2(x,z):
    if int(x+y+z)>int(z+y+x):
        return True
    return False

n=int(input())
arr=sorted(input().rstrip().split(),key=cmp_to_key(cmp))
mn=10e9
y=''


for i in range(n):
    for j in range(n-1):
        if cmp(arr[j],arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

for i in range(n):
    if arr[i][0]!='0':
        break
    y+=arr[i]


ans=inf
if arr[0][0]=='0':
    for i in range(n):
        if arr[i][0]!='0':
            arr[i],arr[0]=arr[0],arr[i]
            #print(arr)
            s=''.join(arr)
            if ans>int(s):
                ans=int(s)
                ansarr=arr[:]
    if ans==inf:
        print('INVALID')
        exit()
    arr=ansarr
    #print(arr)
    for i in range(n):
        for j in range(1,n-1):
            if cmp(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(''.join(arr))
    #print(ans if ans!= inf else 'INVALID')
    
else:
    s=''.join(arr)
    print(s if s[0]!='0' else 'INVALID')
