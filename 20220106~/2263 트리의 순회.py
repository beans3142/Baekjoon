from sys import stdin,setrecursionlimit,maxsize
setrecursionlimit(10**9)
input=stdin.readline

n=int(input())
in_=list(map(int,input().split()))
post_=list(map(int,input().split()))

pos=[0]*(n+1)

for i in range(n):
    pos[in_[i]]=i

def div(in_s,in_e,p_s,p_e):
    if in_s>in_e or p_s>p_e:
        return
    par=post_[p_e]
    print(par,end=' ')
    left=pos[par]-in_s
    right=in_e-pos[par]

    div(in_s,in_s+left-1,p_s,p_s+left-1)
    div(in_e-right+1,in_e,p_e-right,p_e-1)

div(0,n-1,0,n-1)
