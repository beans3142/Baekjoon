import sys
input=sys.stdin.readline
n,m=map(int,input().split())
b=sorted(list(map(int,input().split())))
vi=[]

def bt(idx,arr,V):
    queue=[[idx,arr,V]]
    while queue:
        i,l,v=queue.pop(0)
        print(i,l,v)
        if i == m+1:
            l=list(map(str,l))
            print(' '.join(l[1:]))
        else:
            for _ in range(n):
                if b[_]>=l[-1] and v[_]==0:
                    nv=v
                    nv[_]=1
                    queue.append([i+1,l+[b[_]],nv])
        
    
bt(1,[0],[0]*n)
