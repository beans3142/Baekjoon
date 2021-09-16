from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
item=[]
back=[[0 for i in range(k+1)] for i in range(n)]

for i in range(n):
    item.append(list(map(int,input().split())))

for i in range(n):
    for j in range(1,k+1):
        wei=item[i][0]
        val=item[i][1]

        if j<wei:
            back[i][j]=back[i-1][j]
        else:
            back[i][j]=max(val+back[i-1][j-wei],back[i-1][j])


print(back[-1][-1])
