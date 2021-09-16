from sys import stdin
from collections import defaultdict
input=stdin.readline

n,m,k=map(int,input().split())
built={i:0 for i in range(1,n+1)}
able={i:[] for i in range(1,n+1)}
depth=[0]*(n+1)
unable=False

for i in range(m):
    x,y=map(int,input().split())
    able[x].append(y)
    depth[y]+=1

for i in range(k):
    do,what=map(int,input().split())
    if do==1:
        if depth[what]==0:
            built[what]+=1
            if built[what]==1:
                for j in able[what]:
                    depth[j]-=1
        else:
            unable=True
            break
    else:
        built[what]-=1
        if built[what]==0:
            for j in able[what]:
                depth[j]+=1
        if built[what]<0:
            unable=True
            break

if unable:
    print("Lier!")
else:
    print('King-God-Emperor')
    

