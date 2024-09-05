from sys import stdin
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
w=0.1
center=[0,0]

for i in arr:
    for j in range(2):
        center[j]+=i[j]/n

for i in range(20000):
    mxd=0
    p=[0,0]
    for dot in arr:
        d=sum((center[j]-dot[j])**2 for j in range(2))**0.5
        if d>mxd:
            mxd=d
            p=dot

    for j in range(2):
        center[j]=center[j]+(p[j]-center[j])*w

    w*=0.999

print("%.2f"%(2*mxd),end=" ")
