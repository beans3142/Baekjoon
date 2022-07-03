import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree=[0]*(4*n)

def init():
    for i in range(n-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
        
def query(left,right,n):
    result=0
    left+=n
    right+=n
    while left<right:
        if left%2:
            result+=tree[left]
            left+=1
        if right%2:
            right-=1
            result+=tree[right]
        left//=2
        right//=2
    return result
    

def update(index,val,n):
    index+=n
    tree[index]=val
    while index>1:
        tree[index//2]=tree[index]+tree[index^1]
        index//=2

init()
for i in range(m):
    typ,N,M=map(int,input().split())
    if typ:
        update(N,M,n)
    else:
        s,e=min(N,M),max(N,M)
        print(query(s,e+1,n))
