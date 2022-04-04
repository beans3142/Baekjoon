from sys import stdin
input=stdin.readline

def gettilt(x1,y1,x2,y2):
    return (x2-x1)/(y2-y1)

n=int(input())
arr=sorted([list(map(int,input().split())) for i in range(n)])
hq=[[arr[0][0],arr[0][1]]]
lq=[[arr[0][0],arr[0][1]]]

for i in range(1,n):
    x=arr[i][0]
    y=arr[i][1]
    if hq[0][0]==x:
        hq[0][1]=arr[i][1]
    break

for i in range(1,n):
    ht=gettilt()

for i in range(1,n):
    x=arr[i][0]
    y=arr[i][1]
   # ht=gettilt()
