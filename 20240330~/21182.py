from sys import stdin
input=stdin.readline

n=int(input())
arr=[[],[],[]]
for i in range(n):
    a,b,c=map(float,input().split())
    arr[0].append((a,b))
    arr[1].append((b,c))
    arr[2].append((a,c))

def getdist(arr):
    w=0.1
    center=[0,0]
    for i in arr:
        for j in range(2):
            center[j]+=i[j]/n

    for i in range(2500):
        mxd=0
        p=[0,0]
        for dot in arr:
            d=sum((center[j]-dot[j])**2 for j in range(2))**0.5
            if d>mxd:
                mxd=d
                p=dot

        for j in range(2):
            center[j]=center[j]+(p[j]-center[j])*w

        w*=0.995
    return mxd

ans=min(getdist(arr[0]),getdist(arr[1]),getdist(arr[2]))
print("%.9f"%(ans*2))
