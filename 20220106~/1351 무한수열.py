import sys
input =sys.stdin.readline
n,p,q=map(int,input().split())

arr={0:1}

def dfs(n):
    try:
        if arr[n]!=0:
            return arr[n]
    except:
        pass
    arr[n]=dfs(n//p)+dfs(n//q)
    return arr[n]

print(dfs(n))
