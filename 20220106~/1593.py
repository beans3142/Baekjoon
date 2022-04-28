from sys import stdin
from collections import defaultdict
input=stdin.readline

n,k=map(int,input().split())
s1=input().rstrip()
s2=input().rstrip()
cnt=0
s1c=defaultdict(int)
now=defaultdict(int)

for i in s1:
    s1c[i]+=1

for i in range(len(s1)):
    if s2[i] in s1c:
        now[s2[i]]+=1

ans=0
if len(now)==len(s1c):
    able=True
    for i in s1c:
        if s1c[i]!=now[i]:
            able=False
            break
    ans+=able

for i in range(len(s1),len(s2)):
    if s2[i] in s1c:
        now[s2[i]]+=1
    if s2[i-len(s1)] in s1c:
        now[s2[i-len(s1)]]-=1
        if now[s2[i-len(s1)]]==0:
            del now[s2[i-len(s1)]]
    if len(now)==len(s1c):
        able=True
        for i in s1c:
            if s1c[i]!=now[i]:
                able=False
                break
        ans+=able

print(ans)
