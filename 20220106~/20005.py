from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m,p=map(int,input().split())
queue={chr(97+i):deque([]) for i in range(p)}
matrix=[list(input().rstrip()) for i in range(n)]
vi={chr(97+i):[[0]*m for i in range(n)] for i in range(p)}
end={chr(97+i):False for i in range(p)}
ans=0
dps={}

for i in range(n):
    for j in range(m):
        if 'a'<=matrix[i][j]<='z':
            queue[matrix[i][j]].append([j,i])
            vi[matrix[i][j]][i][j]=1
            matrix[i][j]='.'

for i in range(p):
    a,b=input().rstrip().split()
    dps[a]=int(b)

bosshp=int(input())
totaldps=0

while bosshp>0 and ans<p:
    for player in queue:
        if end[player]==False:
            le=len(queue[player])
            for casecnt in range(le):
                x,y=queue[player].popleft()
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if -1<nx<m and -1<ny<n:
                        if vi[player][ny][nx]==0 and matrix[ny][nx]!='X':
                            if matrix[ny][nx]=='B':
                                ans+=1
                                totaldps+=dps[player]
                                end[player]=True
                                break
                            else:
                                vi[player][ny][nx]=1
                                queue[player].append([nx,ny])
                if end[player]:
                    break
    bosshp-=totaldps

print(ans)
