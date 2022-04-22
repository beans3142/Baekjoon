from sys import stdin
from collections import defaultdict
from heapq import heappop,heappush
input=stdin.readline

inf = float('inf')

def check(cnt,val,nxtdist):
    for i in range(1,cnt+1):
        if vi[i][val]<nxtdist:
            return False
    return True
            
        
def dijkstra():
    
    queue=[(0,s,0)]
    vi[0][s]=0
    
    while queue:
        dist,now,cnt=heappop(queue)
        if dist>vi[cnt][now]:
            continue
        for i in dd[now]:
            nxtdist=dd[now][i]+dist
            if check(cnt+1,i,nxtdist):
                vi[cnt+1][i]=nxtdist
                heappush(queue,(nxtdist,i,cnt+1))

    return vi
            

n,m,k=map(int,input().split())
s,d=map(int,input().split())

dd=[{} for i in range(n+1)]
vi=[[inf for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    dd[a][b]=dd[b][a]=c

dijkstra()
ans=[]

for i in range(1,n+1):
    if vi[i][d]!=inf:
        ans.append([vi[i][d],i])

ans.sort()
print(ans[0][0])

for i in range(k):
    up=int(input())
    mn=inf
    for j in range(len(ans)):
        ans[j][0]+=up*ans[j][1]
        mn=min(mn,ans[j][0])
    print(mn)


'''
5 5 1
1 5
1 2 1
2 4 1
3 4 1
3 5 1
2 3 4
30

4
96
'''
