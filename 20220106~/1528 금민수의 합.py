from sys import *
setrecursionlimit(400000)
input=stdin.readline
n=int(input())
end=False

def dfs(val,fc,sc):
    global end
    if not end:
        if val<n:
            dfs(val+7,fc,sc+1)
            dfs(val+4,fc+1,sc)
        if val==n:
            for i in range(fc):
                print(4,end=' ')
            for i in range(sc):
                print(7,end=' ')
            end=True

dfs(0,0,0)
if not end:
    print(-1)
