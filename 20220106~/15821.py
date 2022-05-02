from sys import stdin
input=stdin.readline

def getdist(x,y):
    return (x**2+y**2)**0.5

n,k=map(int,input().split())
distarr=[]

for i in range(n):
    pi=int(input())
    dots=map(int,input().split())
    mxdist=0
    for j in range(pi):
        mxdist=max(mxdist,getdist(next(dots),next(dots)))
    distarr.append(mxdist)

distarr.sort()
print("%0.2f"%distarr[k-1]**2)
