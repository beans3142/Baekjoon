from sys import stdin
from itertools import combinations
from collections import deque
input=stdin.readline

n,m,d=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]

def getdist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

case=list(combinations(zip(range(m),[n]*m),3))
enemyloc=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            enemyloc.append([j,i])

mx=0
for archers in case:
    kills=0
    lefts=len(enemyloc)
    queue=[]
    alive=[1]*len(enemyloc)
    archerdist=[]
    for archer in archers:
        from_to=[]
        for no,loc in enumerate(enemyloc):
            enemy_x,enemy_y=loc[0],loc[1]
            dist=getdist(archer[0],archer[1],enemy_x,enemy_y)
            left=enemy_x-archer[0]
            from_to.append([dist,left,no,enemy_y])
        archerdist.append(deque(sorted(from_to)))
    while True:
        dead=[]
        out=[]
        for no in range(3):
            while alive[archerdist[no][0][2]]!=1:
                archerdist[no].popleft()
            if archerdist[no][0][0]<=d:
                dead.append(archerdist[no][0][2])
            for i in range(len(archerdist[no])):
                archerdist[no][i][3]+=1
                if archerdist[no][i][3]==n:
                    out.append(archerdist[no][i][2])
                archerdist[no][i][0]-=1
        for i in dead:
            if alive[i]==1:
                lefts-=1
                alive[i]=0
                kills+=1
        for i in out:
            if alive[i]==1:
                lefts-=1
                alive[i]=0
        if lefts==0:
            break
    mx=max(kills,mx)
            
print(mx)
