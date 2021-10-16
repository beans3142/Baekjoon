from sys import stdin
from collections import defaultdict
input=stdin.readline

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    cnt=0
    v=defaultdict(int)
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for n1 in a:
        for n2 in b:
            v[n1^n2]+=1
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    for n1 in c:
        for n2 in d:
            cnt+=v[k^n1^n2]
    print(f'Case #{i+1}: {cnt}')
            
