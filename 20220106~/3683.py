from sys import stdin
input=stdin.readline

def dfs(a):
    if vi[a]:
        return False
    vi[a]=True
    for b in graph[a]:
        if rev[b]==-1 or dfs(rev[b]):
            rev[b]=a
            return True
    return False

for _ in range(int(input())):
    
    c,d,v=map(int,input().split())
    arr=[[0,0,0] for i in range(v+1)]
    rev=[-1]*(v+1)

    graph=[[] for i in range(v+1)]

    for i in range(v):
        a,b=input().rstrip().split()
        if a[0]=='D':
            arr[i+1][2]=1
        else:
            a,b=b,a
        arr[i+1][0]=int(a[1:])
        arr[i+1][1]=int(b[1:])
        
    for i in range(1,v+1):
        for j in range(i+1,v+1):
            if arr[i][2]!=arr[j][2]:
                if arr[i][0]==arr[j][0] or arr[i][1]==arr[j][1]:
                    if arr[i][2]==0:
                        graph[i].append(j)
                    else:
                        graph[j].append(i)

    ans=0
    for i in range(1,v+1):
        if arr[i][2]==0:
            vi=[False]*(v+1)
            if dfs(i):
                ans+=1
            
    print(v-ans)
