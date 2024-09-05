from sys import stdin
input=stdin.readline

def sum(i):
    v=0
    while i>0:
        v+=tree[i]
        i-=(i&-i)
    return v

def update(i,v):
    while i<=n:
        tree[i]+=v
        i+=(i&-i)

n=int(input())
tree=[0]*(n+1)
ans=[0]*n

for tal,idx in sorted([(-int(input()),i) for i in range(1,n+1)]):
    ans[idx-1]=sum(idx-1)+1
    update(idx,1)

print(*ans,sep='\n')
print(tree)