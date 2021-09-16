'''
N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)

'''
n,m,k=map(int,input().split())
matrix=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

visited=[False]*(n+1)

def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if visited[i]==False and matrix[v][i]==1:
            dfs(i)

def bfs(v):
    global visited,matrix
    queue=[v]
    visited[v]=True
    while queue:
        x=queue.pop(0)
        print(x,end=' ')
        for i in range(1,n+1):
            if visited[i]==False and matrix[x][i]==1:
                visited[i]=True
                queue.append(i)

def reset():
    global visited
    for i in range(n+1):
        visited[i]=False
    print()

dfs(k)
reset()
bfs(k)
#'''
