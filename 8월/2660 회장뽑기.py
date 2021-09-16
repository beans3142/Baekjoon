from sys import *
from collections import defaultdict
input=stdin.readline
inf=maxsize

candidate=defaultdict(list)
n=int(input())
rel=[[inf]*n for i in range(n)]

while True:
    a,b=map(lambda x: int(x)-1,input().split())
    if a+b<0:
        break
    rel[a][b]=rel[b][a]=1

for i in range(n):
    rel[i][i]=0
    for j in range(n):
        for k in range(n):
            rel[j][k]=min(rel[j][k],rel[j][i]+rel[i][k])

for i in range(n):
    candidate[max(rel[i])].append(i+1)

min_num=min(candidate)
ans=candidate[min_num]
print(min_num,len(ans))
print(*sorted(ans))
