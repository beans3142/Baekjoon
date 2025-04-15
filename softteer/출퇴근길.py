from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
graph=[[[] for i in range(n+1)] for i in range(2)]

for i in range(m):
    a,b=map(int,input().split())
    graph[0][a].append(b)
    graph[1][b].append(a)
    
start,end=map(int,input().split())
vi=[0]*(n+1)
queue=[(0,start),(1,end),(2,end),(3,end)]
vi[end]|=1
vi[start]|=4
while queue:
    typ,now=queue.pop()
    for nxt in graph[typ%2][now]:
        if vi[nxt]&(1<<typ)==0:
            vi[nxt]|=(1<<typ)
            queue.append((typ,nxt))
            
ans=0
for i in range(1,n+1):
    if i==start or i==end: continue
    if vi[i]==15:
        ans+=1
        
print(ans)
