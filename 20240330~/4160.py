from sys import stdin
from collections import defaultdict
input=stdin.readline

def getcase(s,e):
    def get(p1,p2,idx):
        if idx==e:
            case[p1-p2]=max(p1+p2,case[p1-p2])
            return
        get(p1+arr[idx],p2,idx+1)
        get(p1,p2+arr[idx],idx+1)
        get(p1,p2,idx+1)
    case=defaultdict(int)
    get(0,0,s)
    return case

while True:
    n=int(input())
    if n==0: break
    arr=[int(input()) for i in range(n)]
    ans=0
    first=getcase(0,n//2)
    second=getcase(n//2,n)
    for i in first:
        if i in second:
            ans=max(ans,first[i]+second[i])
    print(sum(arr)-ans)
