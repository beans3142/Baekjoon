from sys import stdin
from collections import defaultdict
input=stdin.readline
n,k=map(int,input().split())
arr=[len(input().rstrip()) for i in range(n)]
q=defaultdict(int)
ans=0
for i in range(1,k+1):
    q[arr[i]]+=1

for i in range(n):
    try:
        ans+=q[arr[i]]
        q[arr[i+1]]-=1
        if i+k+1<n:
            q[arr[i+k+1]]+=1
    except:
        pass
print(ans)
