from sys import stdin
from collections import deque
input=stdin.readline

t=int(input())
tree={}

for i in range(t):
    line=list(map(int,input().split()))
    jungjum=line[0]
    tree[jungjum]=[]
    for j in range(1,len(line)-1,2):
        tree[jungjum].append([line[j],line[j+1]])
         	
def bfs(start):
    v=[0]*100001
    mx_len=0
    queue=deque([[start,0]])
    while queue:
        now,length=queue.popleft()
        v[now]=1
        for node in tree[now]:
            if v[node[0]]!=1:
                queue.append([node[0],length+node[1]])
                if length+node[1]>mx_len:
                    mx_len=length+node[1]
                    start=node[0]
    return start,mx_len

for i in range(2):
	jungjum,mx_len=bfs(jungjum)

print(mx_len)
