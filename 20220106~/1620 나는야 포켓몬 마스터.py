import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pokemon={}
for i in range(1,n+m+1):
    if i <= n:
        name=input().rstrip()
        pokemon[name]=i
        pokemon[str(i)]=name
    if i>n:
        print(pokemon[input().rstrip()])
