n,m=map(int,input().split())
a=[input().split()for i in range(n)]
x=[0,0,0,1,1,1,-1,-1,-1]
y=[0,1,-1,1,0,-1,1,0,-1]
t=int(input())
s=0
for i in range(1,n-1):
    for j in range(1,m-1):
        s+=sorted([int(a[i+y[d]][j+x[d]])for d in range(9)])[4]>=t
print(s)
