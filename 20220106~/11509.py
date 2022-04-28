from sys import stdin
from collections import defaultdict,deque
input=stdin.readline

def find(x,idx):
    while True:
        able=False
        if x-1 in dd:
            for i in dd[x-1]:
                if idx<i and arr[i]!=-1:
                    arr[i]=-1
                    idx=i
                    able=True
                    x-=1
                    break
        if not able:
            break

n=int(input())
arr=list(map(int,input().split()))
cnt=0
dd=defaultdict(deque)

for i in range(n):
    dd[arr[i]].append(i)

order=sorted(dd,reverse=True)

for i in order:
    for j in dd[i]:
        if arr[j]!=-1:
            arr[j]=-1
            find(i,j)
            cnt+=1

print(cnt)
