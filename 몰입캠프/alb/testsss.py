from collections import deque

n=int(input())
result=[]
graph=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for _ in range(n):
  graph.append(list(map(int,input())))

def bfs(x,y):
  cnt=1
  arr=deque([[x,y]])
  graph[x][y]=0
  while arr:
      x,y=arr.popleft()
      for i in range(4):
          nx=x+dx[i]
          ny=y+dy[i]
          if -1<nx<n and -1<ny<n:
              if graph[nx][ny]==1:
                  graph[nx][ny]=0
                  cnt+=1
                  arr.append([nx,ny])
  return cnt
  
for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      result.append(bfs(i,j))

result.sort()

print(len(result))

for i in range(len(result)):
  print(result[i])
