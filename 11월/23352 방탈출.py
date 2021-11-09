from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

n,m=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(n)]
v=[[0 for i in range(m)] for i in range(n)]
group={}
eachroom=defaultdict(int)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
group_no=1

for i in range(n):
    for j in range(m):
        if arr[i][j]!=0:
            tmp=v[i][j]+1
            if eachroom[(j,i)]==0:
                nowno=group_no
                group[nowno]=(0,0)
                group_no+=1
            else:
                nowno=eachroom[(j,i)]
            queue=deque([[j,i,0]])
            endx=j
            endy=i
            v[i][j]+=1
            mx_dist=0
            while queue:
                x,y,dist=queue.popleft()
                eachroom[(x,y)]=nowno
                if dist>mx_dist:
                    endx=x
                    endy=y
                    mx_dist=dist
                elif dist==mx_dist:
                    if arr[endy][endx]<arr[y][x]:
                        endx=x
                        endy=y
                
                for _ in range(4):
                    nx=x+dx[_]
                    ny=y+dy[_]
                    if -1<nx<m and -1<ny<n:
                        if arr[ny][nx]!=0 and v[ny][nx]!=tmp:
                            v[ny][nx]+=1
                            queue.append([nx,ny,dist+1])
            if group[nowno][0]<dist:
                group[nowno]=(dist,arr[endy][endx]+arr[i][j],j,i,endy,endx)
            elif group[nowno][0]==dist:
                group[nowno]=(dist,max(group[nowno][1],arr[endy][endx]+arr[i][j]))
                            
ans_dist=0
ans=0
for i in group:
    if group[i][0]>ans_dist:
        ans_dist=group[i][0]
        ans=group[i][1]
    elif group[i][0]==ans_dist:
        ans=max(ans,group[i][1])

print(ans)
