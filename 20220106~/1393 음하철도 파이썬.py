from sys import stdin
from math import gcd,sqrt
input=stdin.readline
xs,ys=map(int,input().split())
xe,ye,dx,dy=map(int,input().split())
div=gcd(dx,dy)
dx//=div
dy//=div
dist_table=[]

def getdist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

for i in range(100):
    nowx1=xe+dx*i
    nowy1=ye+dy*i
    dist_table.append((getdist(nowx1,nowy1,xs,ys),nowx1,nowy1))

ans=sorted(dist_table)
print(ans[0][1],ans[0][2])
