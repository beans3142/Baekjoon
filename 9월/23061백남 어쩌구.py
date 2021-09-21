from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
item=[]
ans=0

item=[list(map(int,input().split())) for i in range(n)]

k=[int(input()) for i in range(m)]
mx_k=max(k)

back=[[0 for i in range(mx_k+1)] for i in range(n)]
for i in range(n):
    for j in range(1,mx_k+1):
        w=item[i][0]
        v=item[i][1]
        if j<w:
            back[i][j]=back[i-1][j]
        else:
            back[i][j]=max(v+back[i-1][j-w],back[i-1][j])

no=1
for i in range(m):
    val=back[-1][k[i]]/k[i]
    if val>ans:
        ans=val
        no=i+1

print(no)
