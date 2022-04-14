from sys import stdin
input=stdin.readline

def bt(s1,s2,cnt,idx):
    global ans
    if cnt>0:
        ans=min(ans,abs(s2-s1))
    if idx==n:
        return
    bt(s1+arr[idx][0],s2+arr[idx][1],cnt+1,idx+1)
    bt(s1,s2,cnt,idx+1)

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
ans=1e10
bt(0,0,0,0)
print(ans)
