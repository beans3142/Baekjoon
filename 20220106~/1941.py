from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

ans=0
dx=[0,0,-1,1]
dy=[1,-1,0,0]
case={"A":0,"B":0}

def make_correct(idx,le,pos):
    global ans,case
    if case["B"]>3:
        return
    if le==7:
        if case["A"]>=4:
            cnt=check(pos)
            if cnt==7:
                ans+=1
        return
    for i in range(idx,25):
        if vi[i]==0:
            vi[i]=1
            case[arr[i]]+=1
            make_correct(i+1,le+1,pos+[i])
            case[arr[i]]-=1
            vi[i]=0

def check(pos):
    x=pos[0]%5
    y=pos[0]//5
    vis=defaultdict(int)
    vis[pos[0]]=1
    cnt=1
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<5 and -1<ny<5:
                nxt=5*ny+nx
                if vi[nxt]==1 and vis[nxt]==0:
                    vis[nxt]=1
                    cnt+=1
                    queue.append([nxt%5,nxt//5])
    return cnt

arr=[]
for i in range(5):
    arr+=input().rstrip()
vi=[0 for i in range(25)]

make_correct(0,0,[])
print(ans)
