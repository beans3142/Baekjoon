from sys import stdin
input=stdin.readline

def dist(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

def getmx(arr):
    mx=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            mx=max(mx,dist(*arr[i],*arr[j]))
    return mx

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]

dot1=0
dot2=0

for i in range(n):
    for j in range(i+1,n):
        if dist(*arr[dot1],*arr[dot2])<dist(*arr[i],*arr[j]):
            dot1=j
            dot2=i

froms=sorted([[dist(*arr[dot1],*arr[i]),*arr[i]] for i in range(n)])

f=[0]*n
e=[0]*n

for i in range(1,n):
    for j in range(i):
        f[i]=max(dist(*froms[j][1:],*froms[i][1:]),f[i])
    f[i]=max(f[i-1],f[i])

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        e[i]=max(dist(*froms[i][1:],*froms[j][1:]),e[i])
    e[i]=max(e[i],e[i+1])

ans=1e10
for i in range(1,n):
    ans=min(ans,f[i-1]**0.5+e[i]**0.5)
print("%.5f"%ans)
