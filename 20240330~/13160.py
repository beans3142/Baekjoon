from sys import stdin
input=stdin.readline

n=int(input())
arr=[]
arange=[]
for i in range(n):
    s,e=map(int,input().split())
    arr.append((s,0)) #open
    arr.append((e,1)) #close
    arange.append((s,e))
arr.sort()
clique=0
mx=0
idx=0
for now in arr:
    if now[1]:
        clique-=1
    else:
        clique+=1
    if clique>mx:
        mx=clique
        idx=now[0]

ans=[]
for i in range(n):
    if arange[i][0]<=idx and idx<=arange[i][1]:
        ans.append(i+1) 

print(mx)
print(*ans)
