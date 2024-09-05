from sys import stdin
from collections import deque
input=stdin.readline

n,k,s=map(int,input().split())

loc=[list(map(int,input().split())) for i in range(n)]

loc.sort()

ans=0
while loc and loc[-1][0]>s:
    lastd,lastc=loc.pop()
    ans+=(lastd-s)*2*(lastc//k+bool(lastc%k))
    if lastc%k:
        able=k-lastc%k
        while able and loc and loc[-1][0]>s:
            if loc[-1][1]<=able:
                able-=loc[-1][1]
                loc.pop()
            else:
                loc[-1][1]-=able
                break

loc.reverse()

while loc and loc[-1][0]<s:
    lastd,lastc=loc.pop()
    ans+=(s-lastd)*2*(lastc//k+bool(lastc%k))
    if lastc%k:
        able=k-lastc%k
        while able and loc and loc[-1][0]<s:
            if loc[-1][1]<=able:
                able-=loc[-1][1]
                loc.pop()
            else:
                loc[-1][1]-=able
                break

print(ans)
