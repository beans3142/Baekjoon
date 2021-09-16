from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
cnt=0
heavy={i:[] for i in range(1,n+1)}
light={i:[] for i in range(1,n+1)}

for i in range(m):
    a,b=map(int,input().split())
    heavy[a].append(b)
    light[b].append(a)

for i in range(1,n+1):
    if not heavy[i] or not light[i]:
        cnt+=1

print(cnt)
