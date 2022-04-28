from sys import stdin
input=stdin.readline

def check(d1,d2,d3):
    l1=getdist(d1,d2)
    l2=getdist(d2,d3)
    l3=getdist(d1,d3)
    l=sorted([l1,l2,l3])
    if round(l[0]**2+l[1]**2,10)==round(l[2]**2,10):
        return True
    return False

def getdist(d1,d2):
    return ((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)**0.5

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]

cnt=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if check(arr[i],arr[j],arr[k]):
                cnt+=1

print(cnt)
