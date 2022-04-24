from sys import stdin
input=stdin.readline

n=int(input())
cost=list(map(int,input().split()))
value=list(map(int,input().split()))
ans=0

def bt(idx,hp,nowvalue):
    global ans
    if hp<=0:
        return
    if idx==n:
        ans=max(ans,nowvalue)
        return
    bt(idx+1,hp-cost[idx],nowvalue+value[idx])
    bt(idx+1,hp,nowvalue)

bt(0,100,0)

print(ans)
