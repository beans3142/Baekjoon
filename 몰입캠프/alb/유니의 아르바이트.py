from sys import stdin
from heapq import heappop,heappush
input=stdin.readline

n,m=map(int,input().split())
jobs=[[]for i in range(11)]
presum=[[]for i in range(11)]
pq=[]

for i in range(n):
    a,b=map(int,input().split())
    jobs[b].append(a)

for i in range(11):
    jobs[i].sort(reverse=True)

for i in range(11):
    if jobs[i]:
        presum[i].append(jobs[i][0])

for k in range(1,2001):
    for i in range(11):
        if k<len(jobs[i]):
            presum[i].append(presum[i][k-1]+jobs[i][k])

for k in range(1,2001):
    for i in range(11):
        if k<len(jobs[i]):
            presum[i][k]+=(k)*(k+1)

for i in range(11):
    if presum[i]:
        heappush(pq,(-presum[i][0],i,0))

now=0
total=[0]*11

while now<m:
    cost,no,idx=heappop(pq)
    total[no]-=cost
    if idx+1<len(presum[no]):
        val=presum[no][idx+1]-presum[no][idx]
        heappush(pq,(-val,no,idx+1))
    now+=1

print(sum(total))
