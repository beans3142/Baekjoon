import sys
input=sys.stdin.readline
n,m=map(int,input().split())
info={}
for i in range(n+m):
    name=input().rstrip().split()
    if i < n:
        info[name[0]]=name[1]
    else:
        print(info[name[0]])
        
