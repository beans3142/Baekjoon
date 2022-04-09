from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
cnt=0
arr=list(map(int,input().split()))

def bt(s,idx):
    global cnt
    if idx==n:
        if s==k:
            cnt+=1
        return
    bt(s+arr[idx],idx+1)
    bt(s,idx+1)

bt(0,0)

print(cnt if k!=0 else cnt-1)
