from sys import stdin
from collections import deque
input=stdin.readline

arr=[list(map(int,input().split())) for i in range(12)]

case=deque([[1,2],[2,1]])

for i in range(1,6):
    for j in range(2**i):
        now=case.popleft()
        case.append(now+[2*i+1,2*i+2])
        case.append(now+[2*i+2,2*i+1])

mn=1e9
for i in case:
    v=0
    for j in range(1,12):
        v+=arr[i[j-1]-1][i[j]-1]
    mn=min(mn,v)
print(mn)
