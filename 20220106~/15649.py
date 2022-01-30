from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
end=2**m-1

def bt(arr,v):
    if len(arr)>m:
        return
    if len(arr)==m:
        print(*arr)
        return
    for i in range(n):
        if v&(2**i)==0:
            bt(arr+[i+1],v^(2**i))

bt([],0)
