from sys import stdin
input=stdin.readline

def find(x):
    if par[x]==x:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if par[a]<par[b]:
        par[b]=a
    else:
        par[a]=b

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)

def crossed(x1,y1,x2,y2,x3,y3,x4,y4):
    first=ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)
    second=ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)
    if first==0 and second==0:
        if [x1,y1]<=[x4,y4] and [x3,y3]<=[x2,y2]:
            return True
        return False
    else:
        if first<=0 and second<=0:
            return True
        return False

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
arr=sorted([min([x1,y1,x2,y2],[x2,y2,x1,y1]) for x1,y1,x2,y2 in arr])
par=[i for i in range(n+1)]

for i in range(n):
    for j in range(i+1,n):
        if crossed(*arr[i],*arr[j]):
            union(i+1,j+1)

for i in range(n):
    find(i+1)

mx=1
stack=1
par.sort()
for i in range(1,n+1):
    if par[i]==par[i-1]:
        stack+=1
        mx=max(stack,mx)
    else:
        stack=1

print(len(set(par))-1)
print(mx)
