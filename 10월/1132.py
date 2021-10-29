from sys import stdin
from collections import defaultdict,deque
input=stdin.readline

n=int(input())
v=defaultdict(int)
start=defaultdict(int)
ans=0

for i in range(n):
    s=input().rstrip()
    start[s[0]]=1
    for j in range(len(s)):
        v[s[~j]]+=10**j

a=sorted([(v[i],start[i]) for i in v])

num=deque([i for i in range(10-len(a),10)])
for i in range(len(a)):
    if a[i][1]==1 and num[0]==0:
        num[0],num[1]=num[1],num[0]
    ans+=a[i][0]*num.popleft()

print(ans)
