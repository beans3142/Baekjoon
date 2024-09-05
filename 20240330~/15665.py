from sys import stdin
input=stdin.readline

def bt(arr,dep):
    if dep==m:
        print(*arr)
        return
    for i in nums:
        bt(arr+[i],dep+1)

n,m=map(int,input().split())
nums=sorted(set(map(int,input().split())))

bt([],0)
