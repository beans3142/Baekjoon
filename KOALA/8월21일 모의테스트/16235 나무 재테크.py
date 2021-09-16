from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]

n,m,k=map(int,input().split())
s2d2=[list(map(int,input().split())) for i in range(n)]
tree=[[deque() for i in range(n)] for i in range(n)]
yangbun=[[5 for i in range(n)] for i in range(n)]
locate_tree=defaultdict(int)

for i in range(m):
    x,y,z=map(int,input().split())
    tree[x-1][y-1].append(z)
    locate_tree[(y-1,x-1)]=1

for i in range(k):
    death=[]
    marry=[]
    for wood in locate_tree:
        i=wood[1]
        j=wood[0]
        l=len(tree[i][j])
        for k in range(l):
            young=tree[i][j].popleft()
            if yangbun[i][j]<young:
                death.append((j,i,young//2))
                locate_tree[(j,i)]-=1
                continue
            yangbun[i][j]-=young
            young+=1
            tree[i][j].append(young)
            if young%5==0:
                marry.append((j,i))

    for x,y,z in death:
        yangbun[y][x]+=z
        if locate_tree[(x,y)]==0:
            del locate_tree[(x,y)]

    for x,y in marry:
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                tree[ny][nx].appendleft(1)

    for i in range(n):
        for j in range(n):
            yangbun[i][j]+=s2d2[i][j]

    print(locate_tree)
    
cnt=0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            cnt+=len(tree[i][j])

print(cnt)

