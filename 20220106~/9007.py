from sys import stdin
from bisect import *
input=stdin.readline

for _ in range(int(input())):
    k,n=map(int,input().split())
    arr=[[] for i in range(4)]
    for i in range(4):
        arr[i]=list(map(int,input().split()))

    s1=set()
    for i in range(n):
        for j in range(n):
            s1.add(arr[0][i]+arr[1][j])
    a1=sorted(s1)

    s2=set()
    for i in range(n):
        for j in range(n):
            s2.add(arr[2][i]+arr[3][j])
    a2=sorted(s2)


    dif=float('inf')
    ans=0

    for i in a1:
        idx=bisect_left(a2,k-i)
        if idx==len(a2):
            idx-=1
        if dif>abs(k-(a2[idx]+i)):
            dif=abs(k-(a2[idx]+i))
            ans=a2[idx]+i
        elif dif==abs(k-(a2[idx]+i)):
            ans=min(ans,a2[idx]+i)
        if dif>abs(k-(a2[idx-1]+i)):
            dif=abs(k-(a2[idx-1]+i))
            ans=a2[idx-1]+i
        elif dif==abs(k-(a2[idx-1]+i)):
            ans=min(ans,a2[idx-1]+i)

    print(ans)
