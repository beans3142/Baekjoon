from sys import stdin
input=stdin.readline

l,size=map(int,input().split())
m=int(input())
left,right=1,size
totalmove=0

for i in range(m):
    loc=int(input())
    if loc<left:
        right-=left-loc
        totalmove+=left-loc
        left-=left-loc
    elif loc>right:
        left+=loc-right
        totalmove+=loc-right
        right+=loc-right

print(totalmove)
