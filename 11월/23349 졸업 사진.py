from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
p={}
v=defaultdict(int)
voted=defaultdict(int)
pe=defaultdict(dict)
ps=defaultdict(dict)
for i in range(n):
    name,place,start,end=input().rstrip().split()
    start=int(start)
    end=int(end)
    if v[name]:
        continue
    try:
        p[place]
    except:
        p[place]=defaultdict(int)
        pe[place]=defaultdict(int)
        ps[place]=defaultdict(int)
    v[name]=1
    voted[place]+=1
    pe[place][end]+=1
    ps[place][start]+=1
    for j in range(start,end):
        p[place][j]+=1

order=[]
for i in voted:
    order.append([-voted[i],i])

order.sort()
mx=0
ansp=''
anss=0
anse=0
mx=0


for t,i in order:
    if order[0][0]!=t:
        break
    idx=1
    while(idx<50001):
        if mx<p[i][idx]:
            l=0
            ss=idx
            mx=p[i][idx]
            while True:
                idx+=1
                if mx!=p[i][idx]:
                    break
            anss=ss
            ansp=i
            anse=idx
            idx-=1
        else:
            idx+=1

print(ansp,anss,anse)
